const { SecretsManagerClient, GetSecretValueCommand } = require('@aws-sdk/client-secrets-manager');
const logger = require('./helpers/logger');

const client = new SecretsManagerClient({
	region: process.env.AWS_SECRET_MANAGER_REGION
});

const loadSecretVaribles = async () => {
	try {
		const secretId = process.env.AWS_SECRET_MANAGER_ARN;

		const command = new GetSecretValueCommand({ SecretId: secretId });
		const data = await client.send(command);

		if (data.SecretString) {
			const secrets = JSON.parse(data.SecretString);
			Object.entries(secrets).forEach(([key, value]) => {
				process.env[key] = value;
			});
		}
	} catch (e) {
		logger.error('Secret key error', e);
		throw e;
	}
};

module.exports = {
	loadSecretVaribles
};
