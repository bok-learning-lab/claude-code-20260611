/**
 * Shared, module-level constants for the Harvard Art Museums MCP server.
 */
/** Base URL for the main data API (requires an apikey query parameter). */
export declare const API_BASE_URL = "https://api.harvardartmuseums.org";
/** Base URL for the IIIF presentation service (no API key required). */
export declare const IIIF_BASE_URL = "https://iiif.harvardartmuseums.org";
/** Maximum size, in characters, of any single tool response before truncation. */
export declare const CHARACTER_LIMIT = 25000;
/** Default number of records per page when the caller does not specify `size`. */
export declare const DEFAULT_PAGE_SIZE = 10;
/** Maximum records per page accepted by the API. */
export declare const MAX_PAGE_SIZE = 100;
/** Documented courtesy rate limit for the API (requests per day). */
export declare const DAILY_RATE_LIMIT = 2500;
/** HTTP request timeout in milliseconds. */
export declare const REQUEST_TIMEOUT_MS = 30000;
//# sourceMappingURL=constants.d.ts.map