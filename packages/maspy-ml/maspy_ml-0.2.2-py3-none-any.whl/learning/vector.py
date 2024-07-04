from typing import TYPE_CHECKING, Any, Generic, TypeVar

import numpy as np

from maspy.learning.space import Space
from maspy.learning.core import ActType, ObsType, RenderFrame
from maspy.learning.ml_utils import utl_np_random

if TYPE_CHECKING:
    from maspy.learning.registration import EnvSpec
    
ArrayType = TypeVar("ArrayType")

__all__ = [
    "VectorEnv",
    "VectorWrapper",
    "VectorObservationWrapper",
    "VectorActionWrapper",
    "VectorRewardWrapper",
    "ArrayType",
]

class VectorEnv(Generic[ObsType, ActType, ArrayType]):
    
    metadata: dict[str, Any] = {}
    spec: EnvSpec | None = None
    render_mode: str | None = None
    closed: bool = False

    observation_space: Space
    action_space: Space
    single_observation_space: Space
    single_action_space: Space

    num_envs: int

    _np_random: np.random.Generator | None = None
    _np_random_seed: int | None = None
    
    def reset(self, *, seed: int | None = None, options: dict[str, Any] | None = None) -> tuple[ObsType, dict[str, Any]]: #ype: ignore
        if seed is not None:
            self._np_random, np_random_seed = utl_np_random(seed)
            
    def step(self, action: ActType) -> tuple[ObsType, ArrayType, ArrayType, ArrayType, dict[str, Any]]:
        raise NotImplementedError
    
    def render(self) -> tuple[RenderFrame, ...]:
        raise NotImplementedError(
            f"{self.__str__()} render function is not implemented."
        )
    
    def close(self, **kwargs: Any) -> None:
        if self.closed:
            return
        self.close_extras(**kwargs)
        self.closed = True
        
    def close_extras(self, **kwargs: Any):
        pass

    @utl_np_random.setter
    def np_random(self, value: np.random.Generator):
        self._np_random = value
        self._np_random_seed = -1
    
    @property
    def np_random_seed(self) -> int | None:
        if self._np_random_seed is None:
            self._np_random, self._np_random_seed = utl_np_random()
        return self._np_random_seed

    @property
    def unwrapped(self):
        return self

    def _add_info(
        self, vector_infos: dict[str, Any], env_info: dict[str, Any], env_num: int
    ) -> dict[str, Any]:
        for key, value in env_info.items():
            # If value is a dictionary, then we apply the `_add_info` recursively.
            if isinstance(value, dict):
                array = self._add_info(vector_infos.get(key, {}), value, env_num)
            # Otherwise, we are a base case to group the data
            else:
                # If the key doesn't exist in the vector infos, then we can create an array of that batch type
                if key not in vector_infos:
                    if type(value) in [int, float, bool] or issubclass(
                        type(value), np.number
                    ):
                        array = np.zeros(self.num_envs, dtype=type(value))
                    elif isinstance(value, np.ndarray):
                        # We assume that all instances of the np.array info are of the same shape
                        array = np.zeros(
                            (self.num_envs, *value.shape), dtype=value.dtype
                        )
                    else:
                        # For unknown objects, we use a Numpy object array
                        array = np.full(self.num_envs, fill_value=None, dtype=object)
                # Otherwise, just use the array that already exists
                else:
                    array = vector_infos[key]

                # Assign the data in the `env_num` position
                #   We only want to run this for the base-case data (not recursive data forcing the ugly function structure)
                array[env_num] = value

            # Get the array mask and if it doesn't already exist then create a zero bool array
            array_mask = vector_infos.get(
                f"_{key}", np.zeros(self.num_envs, dtype=np.bool_)
            )
            array_mask[env_num] = True

            # Update the vector info with the updated data and mask information
            vector_infos[key], vector_infos[f"_{key}"] = array, array_mask

        return vector_infos

    def __del__(self):
        if not getattr(self, "closed", True):
            self.close()

    def __repr__(self) -> str:
        if self.spec is None:
            return f"{self.__class__.__name__}(num_envs={self.num_envs})"
        else:
            return (
                f"{self.__class__.__name__}({self.spec.id}, num_envs={self.num_envs})"
            )

class VectorWrapper(VectorEnv):
    def __init__(self, env: VectorEnv):
        """Initialize the vectorized environment wrapper.

        Args:
            env: The environment to wrap
        """
        self.env = env
        assert isinstance(env, VectorEnv)

        self._observation_space: Space | None = None
        self._action_space: Space | None = None
        self._single_observation_space: Space | None = None
        self._single_action_space: Space | None = None
        self._metadata: dict[str, Any] | None = None

    def reset(
        self,
        *,
        seed: int | list[int] | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[ObsType, dict[str, Any]]:
        """Reset all environment using seed and options."""
        return self.env.reset(seed=seed, options=options)

    def step(
        self, actions: ActType
    ) -> tuple[ObsType, ArrayType, ArrayType, ArrayType, dict[str, Any]]:
        """Step through all environments using the actions returning the batched data."""
        return self.env.step(actions)

    def render(self) -> tuple[RenderFrame, ...] | None:
        """Returns the render mode from the base vector environment."""
        return self.env.render()

    def close(self, **kwargs: Any):
        """Close all environments."""
        return self.env.close(**kwargs)

    def close_extras(self, **kwargs: Any):
        """Close all extra resources."""
        return self.env.close_extras(**kwargs)

    @property
    def unwrapped(self):
        """Return the base non-wrapped environment."""
        return self.env.unwrapped

    def __repr__(self):
        """Return the string representation of the vectorized environment."""
        return f"<{self.__class__.__name__}, {self.env}>"

    @property
    def observation_space(self) -> Space:
        """Gets the observation space of the vector environment."""
        if self._observation_space is None:
            return self.env.observation_space
        return self._observation_space

    @observation_space.setter
    def observation_space(self, space: Space):
        """Sets the observation space of the vector environment."""
        self._observation_space = space

    @property
    def action_space(self) -> Space:
        """Gets the action space of the vector environment."""
        if self._action_space is None:
            return self.env.action_space
        return self._action_space

    @action_space.setter
    def action_space(self, space: Space):
        """Sets the action space of the vector environment."""
        self._action_space = space

    @property
    def single_observation_space(self) -> Space:
        """Gets the single observation space of the vector environment."""
        if self._single_observation_space is None:
            return self.env.single_observation_space
        return self._single_observation_space

    @single_observation_space.setter
    def single_observation_space(self, space: Space):
        """Sets the single observation space of the vector environment."""
        self._single_observation_space = space

    @property
    def single_action_space(self) -> Space:
        """Gets the single action space of the vector environment."""
        if self._single_action_space is None:
            return self.env.single_action_space
        return self._single_action_space

    @single_action_space.setter
    def single_action_space(self, space):
        """Sets the single action space of the vector environment."""
        self._single_action_space = space

    @property
    def num_envs(self) -> int:
        """Gets the wrapped vector environment's num of the sub-environments."""
        return self.env.num_envs

    @property
    def np_random(self) -> np.random.Generator:
        """Returns the environment's internal :attr:`_np_random` that if not set will initialise with a random seed.

        Returns:
            Instances of `np.random.Generator`
        """
        return self.env.np_random

    @np_random.setter
    def np_random(self, value: np.random.Generator):
        self.env.np_random = value

    @property
    def np_random_seed(self) -> int | None:
        """The seeds of the vector environment's internal :attr:`_np_random`."""
        return self.env.np_random_seed

    @property
    def metadata(self):
        """The metadata of the vector environment."""
        if self._metadata is not None:
            return self._metadata
        return self.env.metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value

    @property
    def spec(self) -> EnvSpec | None:
        """Gets the specification of the wrapped environment."""
        return self.env.spec

    @property
    def render_mode(self) -> tuple[RenderFrame, ...] | None:
        """Returns the `render_mode` from the base environment."""
        return self.env.render_mode

    @property
    def closed(self):
        """If the environment has closes."""
        return self.env.closed

    @closed.setter
    def closed(self, value: bool):
        self.env.closed = value


class VectorObservationWrapper(VectorWrapper):
    """Wraps the vectorized environment to allow a modular transformation of the observation.

    Equivalent to :class:`gymnasium.ObservationWrapper` for vectorized environments.
    """

    def reset(
        self,
        *,
        seed: int | list[int] | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[ObsType, dict[str, Any]]:
        """Modifies the observation returned from the environment ``reset`` using the :meth:`observation`."""
        observations, infos = self.env.reset(seed=seed, options=options)
        return self.observations(observations), infos

    def step(
        self, actions: ActType
    ) -> tuple[ObsType, ArrayType, ArrayType, ArrayType, dict[str, Any]]:
        """Modifies the observation returned from the environment ``step`` using the :meth:`observation`."""
        observations, rewards, terminations, truncations, infos = self.env.step(actions)
        return (
            self.observations(observations),
            rewards,
            terminations,
            truncations,
            infos,
        )

    def observations(self, observations: ObsType) -> ObsType:
        """Defines the vector observation transformation.

        Args:
            observations: A vector observation from the environment

        Returns:
            the transformed observation
        """
        raise NotImplementedError


class VectorActionWrapper(VectorWrapper):
    """Wraps the vectorized environment to allow a modular transformation of the actions.

    Equivalent of :class:`gymnasium.ActionWrapper` for vectorized environments.
    """

    def step(
        self, actions: ActType
    ) -> tuple[ObsType, ArrayType, ArrayType, ArrayType, dict[str, Any]]:
        """Steps through the environment using a modified action by :meth:`action`."""
        return self.env.step(self.actions(actions))

    def actions(self, actions: ActType) -> ActType:
        """Transform the actions before sending them to the environment.

        Args:
            actions (ActType): the actions to transform

        Returns:
            ActType: the transformed actions
        """
        raise NotImplementedError


class VectorRewardWrapper(VectorWrapper):
    """Wraps the vectorized environment to allow a modular transformation of the reward.

    Equivalent of :class:`gymnasium.RewardWrapper` for vectorized environments.
    """

    def step(
        self, actions: ActType
    ) -> tuple[ObsType, ArrayType, ArrayType, ArrayType, dict[str, Any]]:
        """Steps through the environment returning a reward modified by :meth:`reward`."""
        observations, rewards, terminations, truncations, infos = self.env.step(actions)
        return observations, self.rewards(rewards), terminations, truncations, infos

    def rewards(self, rewards: ArrayType) -> ArrayType:
        """Transform the reward before returning it.

        Args:
            rewards (array): the reward to transform

        Returns:
            array: the transformed reward
        """
        raise NotImplementedError