/**
 * Shared HTTP client and error handling for the Harvard Art Museums API.
 */
/** Acceptable values for an API query-string parameter. */
export type QueryValue = string | number | boolean | undefined | null;
/**
 * Read and validate the API key from the environment.
 * @throws Error with an actionable message when HAM_API_KEY is unset.
 */
export declare function getApiKey(): string;
/**
 * Perform a GET request against the API, automatically attaching the API key
 * and dropping any parameters that are undefined, null, or empty strings.
 *
 * @param endpoint API path without a leading slash (e.g. "object" or "object/123").
 * @param params Query parameters to send (apikey is added automatically).
 * @returns The parsed JSON response body.
 */
export declare function hamRequest<T>(endpoint: string, params?: Record<string, QueryValue>): Promise<T>;
/**
 * Convert any thrown error into a clear, actionable, single-line message that
 * guides the agent toward a fix. Internal details are not leaked.
 */
export declare function handleApiError(error: unknown): string;
//# sourceMappingURL=client.d.ts.map