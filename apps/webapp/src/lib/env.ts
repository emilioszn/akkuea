import { validateWebappEnv } from "@stellar-rwa-kit/shared";

// Validate webapp environment variables at boot time
export const env = validateWebappEnv();
