import warnings
from typing import Iterable

from cobamp.core.models import ConstraintBasedModel
from cobamp.core.optimization import Solution, BatchOptimizer
from cobamp.utilities.context import CommandHistory
from cobamp.wrappers.external_wrappers import get_model_reader, AbstractObjectReader
from pathos.multiprocessing import cpu_count

MP_THREADS = cpu_count()
INF = float('inf')
DEFAULT_EPS = 1e-6


class Task(object):
    """
    A task is a set of constraints that can be applied to a model. It is defined by a set of reactions, a set of
    constraints on the fluxes of these reactions, a set of constraints on the inflow and outflow of metabolites, and
    a set of mandatory activities that must be present in the solution. A task can be evaluated on a model to determine
    if the model satisfies the task.

    """
    __defaults__ = {
        'should_fail': False,
        'reaction_dict': {},
        'inflow_dict': {},
        'outflow_dict': {},
        'flux_constraints': {},
        'mandatory_activity': [],
        'name': 'default_task',
        'annotations': {}
    }

    __types__ = {
        'reaction_dict': dict,
        'inflow_dict': dict,
        'outflow_dict': dict,
        'should_fail': bool,
        'name': str,
        'flux_constraints': dict,
        'annotations': dict,
        'mandatory_activity': list
    }

    def __init__(self, **kwargs):
        """
        reaction_dict: rxd = {'r1':({'m1':-1, 'm2':2}, (lb, ub)), ... }
        inflow_dict: ifd = {'m3':(1,1), ... }
        outflow_dict: ofd = {'m5':(5,5), ... }

        """
        for k, v in self.__defaults__.items():
            itype, dval = self.__types__[k], self.__defaults__[k]
            setattr(self, k, dval if k not in kwargs.keys() else kwargs[k])

    def combine(self, other, add: bool = True):
        """
        Combine two tasks into a single task. The resulting task will have the same failure criteria as the original

        Parameters
        ----------
        other: Task
            The task to combine with
        add: bool
            If True, the resulting task will be the sum of the two tasks. If False, the resulting task will be the

        Returns
        -------
        Task: The combined task

        """
        assert isinstance(other, Task), 'Could not apply + operator between types Task and ' + str(type(other))
        assert self.should_fail == other.should_fail, 'Tasks with different failure criteria cannot be added'

        def bound_dict_add(lst):
            ndict = {}
            for dct in lst:
                for k, d in dct.items():
                    if k not in ndict.keys():
                        ndict[k] = d
                    else:
                        ndict[k][0] += max((d[0] if add else -d[0]), 0)
                        ndict[k][1] += max((d[1] if add else -d[0]), 0)
            return ndict

        shfail = self.should_fail
        rx_dict = {k: v for k, v in list(self.reaction_dict.items()) + list(other.reaction_dict.items())}
        flx_dict = bound_dict_add([self.flux_constraints, other.flux_constraints])
        in_dict = bound_dict_add([self.inflow_dict, other.inflow_dict])
        out_dict = bound_dict_add([self.outflow_dict, other.outflow_dict])
        mnd_act = set(self.mandatory_activity) | set(other.mandatory_activity)
        name = (' minus ' if not add else ' plus ').join([self.name, other.name])
        annotations = {}
        if self.name not in self.annotations:
            annotations[self.name] = self.annotations
        annotations[other.name] = other.annotations

        return shfail, rx_dict, flx_dict, in_dict, out_dict, mnd_act, name, annotations

    def combine_inplace(self, other, add: bool = True):
        """
        Combine two tasks into a single task. The resulting task will have the same failure criteria as the original

        Parameters
        ----------
        other: Task
            The task to combine with
        add: bool
            If True, the resulting task will be the sum of the two tasks. If False, the resulting task will be the

        Returns
        -------
        Task: The combined task

        """
        shfail, rx_dict, flx_dict, in_dict, out_dict, mnd_act, name, annotations = self.combine(other, add)
        self.should_fail = shfail
        self.reaction_dict = rx_dict
        self.flux_constraints = flx_dict
        self.outflow_dict = out_dict
        self.inflow_dict = in_dict
        self.mandatory_activity = mnd_act
        self.name = name
        self.annotations = annotations

    def __add__(self, other):
        shfail, rx_dict, flx_dict, in_dict, out_dict, mnd_act, name, annotations = self.combine(other, True)
        return Task(should_fail=shfail, reaction_dict=rx_dict, flux_constraints=flx_dict, inflow_dict=in_dict,
                    outflow_dict=out_dict, mandatory_activity=mnd_act, name=name, annotations=annotations)

    def __sub__(self, other):
        shfail, rx_dict, flx_dict, in_dict, out_dict, mnd_act, name, annotations = self.combine(other, False)
        return Task(should_fail=shfail, reaction_dict=rx_dict, flux_constraints=flx_dict, inflow_dict=in_dict,
                    outflow_dict=out_dict, mandatory_activity=mnd_act, name=name, annotations=annotations)

    def __iadd__(self, other):
        self.combine_inplace(other, True)
        return self

    def __isub__(self, other):
        self.combine_inplace(other, False)
        return self

    @property
    def should_fail(self):
        return self.__should_fail

    @should_fail.setter
    def should_fail(self, value):
        self.__should_fail = value

    @property
    def reaction_dict(self):
        return self.__reaction_dict

    @reaction_dict.setter
    def reaction_dict(self, value):
        self.__reaction_dict = value

    @property
    def flux_constraints(self):
        return self.__flux_constraints

    @flux_constraints.setter
    def flux_constraints(self, value):
        self.__flux_constraints = value

    @property
    def outflow_dict(self):
        return self.__outflow_dict

    @outflow_dict.setter
    def outflow_dict(self, value):
        self.__outflow_dict = value

    @property
    def inflow_dict(self):
        return self.__inflow_dict

    @inflow_dict.setter
    def inflow_dict(self, value):
        self.__inflow_dict = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def annotations(self):
        return self.__annotations

    @annotations.setter
    def annotations(self, value):
        self.__annotations = value

    @property
    def mandatory_activity(self):
        return self.__mandatory_activity

    @mandatory_activity.setter
    def mandatory_activity(self, value):
        self.__mandatory_activity = value

    def id_replace(self, func):
        """
        Replace the identifiers in the task with the result of a function applied to the identifiers

        Parameters
        ----------
        func: function
            The function to apply to the identifiers

        """
        for prop, typ in self.__types__.items():
            prop_data = getattr(self, prop)
            if typ == list:
                setattr(self, prop, [func(k) for k in prop_data])
            elif typ == dict and prop != 'annotations':
                setattr(self, prop, {func(k): v for k, v in prop_data.items()})
            else:
                pass

    def get_add_reaction_args(self, model: ConstraintBasedModel, closed: bool = False) -> (dict, set):
        """
        Get the arguments to add the reactions to the model

        Parameters
        ----------
        model: ConstraintBasedModel
            The model to add the reactions to
        closed: bool
            Whether to add the reactions as closed or open

        Returns
        -------
        dict, set: The arguments to add the reactions to the model, and the set of reactions that were added

        """

        ## assume list order is arg, bounds. keys contain the name
        ## reaction_dict - add reactions to the model

        reactions = {}
        for k, v in self.reaction_dict.items():
            reaction_name = '_'.join([self.name, k, 'task_reaction'])
            if reaction_name not in model.reaction_names:
                reactions[reaction_name] = [v[0], (0, 0) if closed else v[1], reaction_name]

        ## flow_dict - add drains to the model
        for k, v in self.inflow_dict.items():
            sink_name = '_'.join([k, 'inflow'])
            if sink_name not in model.reaction_names:
                reactions[sink_name] = [{k: 1}, (0, 0) if closed else v, sink_name]

        for k, v in self.outflow_dict.items():
            sink_name = '_'.join([k, 'outflow'])
            if sink_name not in model.reaction_names:
                reactions[sink_name] = [{k: -1}, (0, 0) if closed else v, sink_name]

        # reaction_names = list(reactions.keys())
        # arg, bounds = zip(*[reactions[k] for k in reaction_names])
        #
        # call_args = {'arg':arg, 'bounds':bounds, 'names': reaction_names}
        added_rxs = set(reactions.keys())

        return reactions, added_rxs

    def get_add_reaction_cmds(self, model: ConstraintBasedModel, closed: bool = False) -> (CommandHistory, set):
        """
        Get the commands to add the reactions to the model

        Parameters
        ----------
        model: ConstraintBasedModel
            The model to add the reactions to
        closed: bool
            Whether to add the reactions as closed or open

        Returns
        -------
        CommandHistory, set: The commands to add the reactions to the model, and the set of reactions that were added

        """
        ## reaction_dict - add reactions to the model

        command_history = CommandHistory()
        args, added_rx = self.get_add_reaction_args(model, closed)
        ordered_rx_names = list(added_rx)
        arg, bnd = list(zip(*[args[k] for k in ordered_rx_names]))
        command_history.queue_command(model.add_reactions, {'args': arg, 'bounds': bnd, 'names': ordered_rx_names})

        return command_history, added_rx

    def get_task_bounds(self) -> dict:
        """
        Get the bounds for the task

        Returns
        -------
        dict: The bounds for the task

        """
        master_dict = {}
        reac_bounds = {'_'.join([self.name, k, 'task_reaction']): v[1] for k, v in self.reaction_dict.items()}
        inflow_bounds = {'_'.join([k, 'inflow']): v for k, v in self.inflow_dict.items()}
        outflow_bounds = {'_'.join([k, 'outflow']): v for k, v in self.outflow_dict.items()}
        aflx_bounds = {k: (v[0], v[1]) for k, v in self.flux_constraints.items()}
        for d in [reac_bounds, inflow_bounds, outflow_bounds, aflx_bounds]:
            master_dict.update(d)

        return master_dict

    ## constraint_dict - impose additional bounds

    @property
    def involved_reactions(self) -> set:
        """
        Get the set of reactions involved in the task

        Returns
        -------
        set: The set of reactions involved in the task

        """
        return set(self.flux_constraints.keys()) | set(self.mandatory_activity)

    def apply_evaluate(self, model: ConstraintBasedModel) -> (bool, dict):
        """
        Apply the task to the model and evaluate the solution

        Parameters
        ----------
        model:  ConstraintBasedModel
            The model to apply the task to

        Returns
        -------
        bool, dict: Whether the task was satisfied, and the expected activity of the mandatory reactions

        """
        involved_reactions_in_model = len(self.involved_reactions - set(model.reaction_names)) == 0
        task_evaluation = False
        if involved_reactions_in_model:
            with model as task_model:
                commands, _ = self.get_add_reaction_cmds(task_model)
                commands.execute_all(True)
                for k, v in self.get_task_bounds():
                    lb, ub = v
                    task_model.set_reaction_bounds(k, lb=lb, ub=ub)
                task_evaluation, expected = self.evaluate_solution(task_model.optimize())
        return task_evaluation & involved_reactions_in_model, expected

    def evaluate_solution(self, sol: Solution, ftol: float = 1e-6) -> (bool, dict):
        """
        Evaluate the solution to the task

        Parameters
        ----------
        sol: Solution
            The solution to evaluate
        ftol: float
            The tolerance for the fluxes

        Returns
        -------
        bool, dict: Whether the task was satisfied, and the expected activity of the mandatory reactions

        """
        is_optimal = sol.status() == 'optimal'
        expected_activity = {k: abs(sol[k]) > ftol for k in self.mandatory_activity}
        # mandatory_are_valid = len([k for k,v in expected_activity.items() if v]) == len(self.mandatory_activity)

        if self.should_fail:
            task_eval = not is_optimal
        else:
            task_eval = is_optimal

        return task_eval, expected_activity

    def __repr__(self):
        name = "Task '" + self.name
        desc = ''
        info = ' ; '.join([k + ': ' + str(len(getattr(self, k))) for k, t in self.__types__.items() if t in [dict, list]
                           and len(getattr(self, k)) > 0])
        fail = "'" + (' expecting failure' if self.should_fail else ' expecting success') + ":"
        if hasattr(self, 'annotations') and 'description' in self.annotations:
            desc = self.annotations['description']
        return name + fail + info + ' -- ' + desc


class TaskEvaluator(object):
    """
    A task evaluator is a wrapper around a model that allows the evaluation of tasks on the model. It can be used to
    evaluate a single task, or to evaluate a batch of tasks on a batch of models.

    Parameters
    ----------
    model: ConstraintBasedModel
        The model to evaluate tasks on
    tasks: Iterable[Task]
        The tasks to evaluate on the model
    solver: str
        The solver to use for the model
    S: np.ndarray
        The stoichiometric matrix
    lb: np.ndarray
        The lower bounds for the reactions
    ub: np.ndarray
        The upper bounds for the reactions
    rxn: np.ndarray
        The reaction names
    mtn: np.ndarray
        The metabolite names

    """
    def __init__(self, **kwargs):
        if 'solver' in kwargs:
            solver = kwargs['solver']
        else:
            solver = None

        if 'model' in kwargs.keys():
            model_obj = kwargs['model']
            if isinstance(model_obj, ConstraintBasedModel):
                self.model = model_obj
            elif isinstance(model_obj, AbstractObjectReader):
                self.model = model_obj.to_cobamp_cbm(solver if solver is not None else True)
            else:
                self.model = get_model_reader(model_obj).to_cobamp_cbm(solver)
        else:
            if 'lb' in kwargs.keys():
                S, lb, ub, rxn, mtn = [kwargs[k] for k in ['S', 'lb', 'ub', 'reaction_names', 'metabolite_names']]
                bounds = list(zip(lb, ub))

                self.model = ConstraintBasedModel(S, bounds, rxn, mtn, True, solver)

        self.__tasks = {}
        self.__original_bounds = {k: v for k, v in zip(self.model.reaction_names, self.model.bounds)}
        self.__task_rxs = {}
        self.__activated_task = None

        if 'tasks' in kwargs:
            self.tasks = kwargs['tasks']
        self.history = None

    @property
    def current_task(self):
        return self.__activated_task

    @current_task.setter
    def current_task(self, value: str):
        self.__disable_tasks(self.model)
        if value is not None:
            self.__enable_task(value, self.model)

    def __enable_task(self, name: str, model: ConstraintBasedModel):
        bounds = self.__tasks[name].get_task_bounds()
        for k, v in bounds.items():
            lb, ub = v
            model.set_reaction_bounds(k, lb=lb, ub=ub)
        self.__activated_task = name

    def __disable_tasks(self, model: ConstraintBasedModel):
        for k, v in self.__original_bounds.items():
            lb, ub = v
            model.set_reaction_bounds(k, lb=lb, ub=ub)
        for k, v in self.__task_rxs.items():
            model.set_reaction_bounds(k, lb=0, ub=0)
        self.__activated_task = None

    def __apply(self, func):
        with self.model as amodel:
            return func(amodel)

    def evaluate(self, context_function=None, flux_distribution_func=None) -> (bool, Solution):
        """
        Evaluate the current task on the model

        Parameters
        ----------
        context_function: function
            A function to apply to the model prior to evaluation
        flux_distribution_func: function
            A function to apply to the model to get the flux distribution

        Returns
        -------
        bool, Solution: Whether the task was satisfied, and the solution to the model

        """
        def apply_eval(model):
            return self.__inner_evaluate(model, context_function, flux_distribution_func)

        if context_function is None:
            return apply_eval(self.model)
        else:
            return self.__apply(apply_eval)

    def batch_evaluate(self, bound_changes: dict, threads: int = MP_THREADS, output_sol: bool = False,
                       mp_batch_size: int = 5000) -> dict:
        """
        Evaluate a batch of tasks on the model

        Parameters
        ----------
        bound_changes: dict
            The changes to apply to the model
        threads: int
            The number of threads to use
        output_sol: bool
            Whether to output the solution
        mp_batch_size: int
            The batch size for multiprocessing

        Returns
        -------
        dict: The results of the evaluation

        """
        self.current_task = None
        cobamp_model = self.model
        task_bounds = {k: v.get_task_bounds() for k, v in self.__tasks.items()}

        bound_change_runs = {}
        for k, tb in task_bounds.items():
            for i, bc in enumerate(bound_changes):
                fd = {}
                fd.update(tb)
                fd.update(bc)
                bound_change_runs[(i, k)] = {cobamp_model.map_labels['reaction'][x]: y for x, y in fd.items()}

        objective_sense = [False] * len(bound_change_runs)
        objective_coef = [{0: 1}] * len(bound_change_runs)
        bc_names = list(bound_change_runs.keys())
        bc_runs = [bound_change_runs[k] for k in bc_names]
        del bound_change_runs
        cobamp_model.initialize_optimizer()
        bopt = BatchOptimizer(linear_system=cobamp_model.model, threads=threads)
        res_dict = {i: {} for i in range(len(bound_changes))}
        ind = 0
        while ind < len(bc_runs):
            sols = dict(zip(bc_names[ind:ind + mp_batch_size],
                            bopt.batch_optimize(bc_runs[ind:ind + mp_batch_size],
                                                objective_coef[ind:ind + mp_batch_size],
                                                objective_sense[ind:ind + mp_batch_size])))
            ind += mp_batch_size
            for k, sol in sols.items():
                i, tn = k
                truth, expected = self.__tasks[tn].evaluate_solution(sol)
                res_dict[i][tn] = (truth, expected, sol if output_sol else None)

        return res_dict

    @staticmethod
    def batch_function(task: Task, params: dict) -> (bool, Solution):
        """
        Evaluate a task on a model

        Parameters
        ----------
        task: Task
            The task to evaluate
        params: dict
            The parameters to use for evaluation

        Returns
        -------
        bool, Solution: Whether the task was satisfied, and the solution to the model

        """
        params['tev'].current_task = task
        cfunc, fdfunc = [params[k] if k in params else None for k in ['context_func', 'flux_distribution_func']]
        return params['tev'].evaluate(cfunc, fdfunc)

    def __inner_evaluate(self, model: ConstraintBasedModel, context_func, flux_distribution_func) -> (bool, Solution):
        """
        Evaluate the current task on the model

        Parameters
        ----------
        model: ConstraintBasedModel
            The model to evaluate the task on
        context_func: function
            A function to apply to the model prior to evaluation
        flux_distribution_func: function
            A function to apply to the model to get the flux distribution

        Returns
        -------
        bool, Solution: Whether the task was satisfied, and the solution to the model

        """
        if self.__activated_task is not None:
            task_to_eval = self.__tasks[self.__activated_task]

            if context_func is not None:
                context_func(model)

            involved_reactions = task_to_eval.involved_reactions

            involved_reactions_in_model = len(involved_reactions - set(model.reaction_names)) == 0

            if flux_distribution_func is not None:
                sol = flux_distribution_func(model)
            else:
                _, nflows = task_to_eval.get_add_reaction_args(model)

                self.model.set_objective({k: 1 for k in nflows})
                sol = model.optimize()

            # evaluation, expected = task_to_eval.evaluate_solution(sol) if involved_reactions_in_model else (False, {})
            evaluation, expected = task_to_eval.evaluate_solution(sol)

            if not involved_reactions_in_model:
                warnings.warn('Task ' + task_to_eval.name + ' has references to missing reactions and was evaluated as '
                                                            'False by default')

            return evaluation, sol, expected
        else:
            warnings.warn('No task is currently active. A loaded task must be activated prior to evaluation using the '
                          'current_task setter (.current_task = task_name')

    @property
    def tasks(self) -> Iterable[Task]:
        """
        Get the tasks

        Returns
        -------
        list: The tasks

        """
        return [n for n in self.__tasks.keys()]

    @tasks.setter
    def tasks(self, value: Iterable[Task]):
        """
        Set the tasks

        Parameters
        ----------
        value: Iterable[Task]
            The tasks to set

        """
        ## TODO: improve task setter with an efficient method for adding reactions at once
        for tn in self.tasks:
            self.__remove_task(tn)

        self.__tasks = {k.name: k for k in value}

        # for t in value:
        # 	self.__populate_task(t)
        self.__populate_tasks(value)

    def __remove_task(self, task_name: Task):
        """
        Remove a task from the model

        Parameters
        ----------
        task_name: str
            The name of the task to remove

        """
        to_remove = []
        for k, v in self.__task_rxs.items():
            if task_name in v and len(v) <= 1:
                to_remove.append(k)
                v.remove(task_name)

        self.model.remove_reactions(to_remove)
        self.__task_rxs = {k: v for k, v in self.__task_rxs.items() if len(v) > 0}
        self.__tasks = {k: v for k, v in self.__tasks.items() if k != task_name}

    def __populate_task(self, task: Task):
        """
        Populate a task

        Parameters
        ----------
        task: Task
            The task to populate

        """
        cmds, rxs = task.get_add_reaction_cmds(self.model, True)
        involved_reactions_in_model = len(task.involved_reactions - set(self.model.reaction_names)) == 0
        cmds.execute_all(True)
        for k in rxs:
            if k not in self.__task_rxs.keys():
                self.__task_rxs[k] = [task.name]
            else:
                self.__task_rxs[k].append(task.name)

        if not involved_reactions_in_model:
            warnings.warn(
                'Task object with name ' + task.name + ' refers to reactions that are not present in the model. '
                                                       'This task will be loaded but will never evaluate as True')

    def __populate_tasks(self, tasks: Iterable[Task]):
        """
        Populate a set of tasks

        Parameters
        ----------
        tasks: Iterable[Task]
            The tasks to populate

        """
        k_names = ['args', 'bounds', 'names']
        add_rx_args = {k: [] for k in k_names}
        for task in tasks:
            arg_list, rxs_to_add = task.get_add_reaction_args(self.model, True)
            for k in rxs_to_add:
                if k not in self.__task_rxs.keys():
                    self.__task_rxs[k] = [task.name]
                    for kp, vp in zip(k_names, arg_list[k]):
                        add_rx_args[kp].extend([vp])
                else:
                    self.__task_rxs[k].append(task.name)
        self.model.add_reactions(**add_rx_args)


if __name__ == '__main__':
    from numpy import array

    S = array([[1, -1, 0, 0, -1, 0, -1, 0, 0],
               [0, 1, -1, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 1, -1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, -1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, -1, 0],
               [0, 0, 0, 0, 1, 0, 0, 1, -1]])

    rx_names = ["R" + str(i) for i in range(1, 10)]
    mt_names = ["M" + str(i) for i in range(1, 7)]

    irrev = [0, 1, 2, 4, 5, 6, 7, 8]
    bounds = [(0 if i in irrev else -1000, 1000) for i in range(9)]
    lb, ub = list(zip(*bounds))
    T = array([0] * S.shape[1]).reshape(1, S.shape[1])
    T[0, 8] = -1
    b = array([-1]).reshape(1, )

    # tasks = TaskEvaluator(S, lb, ub, rx_names, mt_names)
    from cobamp.core.models import ConstraintBasedModel

    cbm = ConstraintBasedModel(S, list(zip(lb, ub)), rx_names, mt_names)

    task = Task(
        should_fail=False,
        inflow_dict={'glucose': [0, 5]},
        outflow_dict={'etanol': [3, 5]},
        # 'm1 => 2 m2'
        reaction_dict={'r1':
                           ({'m1': -1, 'm2': 2}, (0, 1000))}
    )

    from troppo.tasks.task_io import JSONTaskIO

    print(JSONTaskIO().write_to_string([task, task]))
    tasks = [Task(
        flow_dict={'M4': (-4, -4)},
        should_fail=False,
        flux_constraints={'R2': (i, 10)},
        name=str(i)) for i in range(11)]

    tev = TaskEvaluator(model=cbm, tasks=tasks)
    for task in tev.tasks:
        tev.current_task = task
        print(task, tev.evaluate())
