from os import getenv
from flask import Flask
from mediatr import Mediator
from dotenv import load_dotenv

from commands.merge_stage_with_bank_command import MergeStageWithBankCommand
from command_handlers.merge_stage_with_bank_command_handler import MergeStageWithBankCommandHandler
from services.health_check import HealthChecker
from services.stream_branch_manager_service import StreamBranchManagerService
from services.user_authorization_service import UserAuthorizationService


load_dotenv('.env')
app = Flask(__name__)
mediator = Mediator()

@app.before_first_request
def register():
    UserAuthorizationService().register()
    StreamBranchManagerService().register()

@app.route("/refresh_material_bank")
def refresh_material_bank():
    try:
        return mediator.send(MergeStageWithBankCommand())
    except:
        return 'error'
    
@app.route('/health')
def health_check() -> str:
    return HealthChecker.check_health()

if __name__ == "__main__":
    app.run(debug=True, port=getenv("PORT", 5100))
