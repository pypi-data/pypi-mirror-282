from mbodied.agents.motion.motor_agent import MotorAgent
from mbodied.types.motion_controls import HandControl, JointControl, Motion, Pose6D
from mbodied.types.sense.vision import Image


class OpenVlaAgent(MotorAgent):
    """OpenVLA agent to generate robot actions.

    Specify gradio server endpoint in model_src to make inference via API.
    See openvla_example_server.py for the an exmaple of the gradio server code.

    `actor` is a gradio server taking: image, instruction, and unnorm_key as input.

    Example:
        >>> openvla_agent = OpenVlaAgent(model_src="https://api.mbodi.ai/community-models/")
        >>> openvla.act("move hand forward", Image(size=(224, 224)))
        HandControl(pose=Pose6D(x=1,y=2,z=3,roll=0,pitch=0,yaw=0), grasp=JointControl(value=0))
    """

    def __init__(
        self,
        recorder="omit",
        recorder_kwargs=None,
        model_src=None,
        model_kwargs=None,
        local_only: bool = False,
        **kwargs,
    ):
        super().__init__(
            recorder=recorder,
            recorder_kwargs=recorder_kwargs,
            model_src=model_src,
            model_kwargs=model_kwargs,
            local_only=local_only,
            **kwargs,
        )

    def act(self, instruction: str, image: Image, unnorm_key: str = "bridge_orig") -> Motion:
        """Act based on the instruction and image using the remote server."""
        if self.actor is None:
            raise ValueError("Remote actor for OpenVLA not initialized.")
        response = self.actor.act(image.base64, instruction, unnorm_key)
        items = response.strip("[]").split()
        action = [float(item) for item in items]
        return HandControl.unflatten(action)


# Example usage:
if __name__ == "__main__":
    openvla_agent = OpenVlaAgent(model_src="https://api.mbodi.ai/community-models/")
    image = Image("resources/xarm.jpeg")
    response = openvla_agent.act("move forward", image)
    print(response) # noqa
