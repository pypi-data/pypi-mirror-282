import os

current_dir = os.path.dirname(os.path.abspath(__file__))

task_definitions = {
    "5b295021-8df7-40a1-a45e-fe7109ae3902": os.path.join(
        current_dir, "jobs/fazer_pudim.py"
    ),
    "a0788650-de48-454f-acbf-3537ead2d8ed": os.path.join(
        current_dir, "jobs/login_emsys.py"
    ),
}
