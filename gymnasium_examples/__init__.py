from gymnasium.envs.registration import register

register(
    id="gymnasium_examples/GridWorld-v0",
    entry_point="gymnasium_examples.envs:GridWorldEnv",
)
