# Create-User

## Installation And Deployment

Run Files in scripts folder as per below sequence:

```bash
- scripts/initializations.sh (create and activate env)
- scripts/deploy_role.bat (Deploy IAM role on AWS)
- scripts/build_deploy.bat (Deploy API and Lambda using SAM)
```

Note:- Before running aws command make sure to configure aws cli with Access Key And ID.


## Unnitest

Run below command to run pytest for integration testing and code coverage report.

#####python -m pytest --cov=./ --cov-report=html
