from .command_type import Command
from .create_deployment_wizard import CreateDeploymentWizard
from .create_deployment_settings import CreateDeploymentSettings
from .list_deployments import ListDeployments
from .configure_aws_profile import ConfigureAwsProfile
from .configure_deployment_domain import ConfigureDeploymentDomain
from .create_deployment_certificate import CreateDeploymentCertificate
from .deploy_vpc import DeployVpc
from .deploy_auth_userpool import DeployAuthUserPool
from .deploy_api import DeployApi
from .deploy_alerts import DeployAlerts
from .deploy_github import DeployGithub
from .deploy_deployment import DeployDeployment
from .generate_templates import GenerateTemplates

COMMANDS: list[Command] = [
    CreateDeploymentWizard(),
    CreateDeploymentSettings(),
    ListDeployments(),
    ConfigureAwsProfile(),
    ConfigureDeploymentDomain(),
    CreateDeploymentCertificate(),
    DeployVpc(),
    DeployAuthUserPool(),
    DeployApi(),
    DeployAlerts(),
    DeployGithub(),
    DeployDeployment(),
    GenerateTemplates(),
]


def get_command(name: str) -> Command:
    command = next((c for c in COMMANDS if c.get_name() == name), None)
    if command is None:
        print("Command with the specified name not found:", name)
        raise Exception("Command not found")
    return command
