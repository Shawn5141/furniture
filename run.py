from method.main import run
import env
from config import create_parser
from method.config import add_method_arguments

if __name__ == "__main__":
    # default arguments
    parser = create_parser()

    # arguments related to RL/IL methods
    add_method_arguments(parser)

    # change default values
    parser.set_defaults(wandb_project="bimanual")
    parser.set_defaults(rollout_length=200)

    run(parser)
