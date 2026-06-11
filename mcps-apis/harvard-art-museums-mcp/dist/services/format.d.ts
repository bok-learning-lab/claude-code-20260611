/**
 * Shared formatting, pagination, and truncation helpers used by every tool.
 */
import type { HamInfo } from "../types.js";
/** Output format supported by every data-returning tool. */
export declare enum ResponseFormat {
    MARKDOWN = "markdown",
    JSON = "json"
}
/** Normalized pagination metadata derived from an API `info` block. */
export interface PageMeta {
    total: number;
    pages: number;
    page: number;
    count: number;
    has_more: boolean;
    next_page: number | null;
}
/**
 * Derive consistent pagination metadata from an API `info` block.
 *
 * @param info The `info` block from a list response (may be undefined).
 * @param requestedPage The page the caller asked for, used as a fallback.
 * @param count Number of records actually present in this response.
 */
export declare function pageMeta(info: HamInfo | undefined, requestedPage: number, count: number): PageMeta;
/**
 * Render a list of items to a string, shrinking the item set until the result
 * fits within CHARACTER_LIMIT. The render callback receives the (possibly
 * reduced) items and a `truncated` flag so it can include a clear notice and
 * pagination guidance when data was dropped.
 *
 * @param items All items that could be shown.
 * @param render Builds the output string for a given slice of items.
 */
export declare function fitToLimit<T>(items: T[], render: (items: T[], truncated: boolean) => string): string;
/**
 * Collapse whitespace and clip free text to a maximum length, appending an
 * ellipsis when clipped. Returns null for empty/missing input.
 */
export declare function truncateText(value: string | null | undefined, max?: number): string | null;
/** Strip HTML tags from a string (used to clean rich-text catalogue fields). */
export declare function stripHtml(value: string | null | undefined): string | null;
/** Build a standard MCP text tool result. */
export declare function toolText(text: string, isError?: boolean): {
    isError?: boolean | undefined;
    content: {
        type: "text";
        text: string;
    }[];
};
/** A single line in a markdown bullet list, omitted when the value is empty. */
export declare function bullet(label: string, value: unknown): string | null;
//# sourceMappingURL=format.d.ts.map