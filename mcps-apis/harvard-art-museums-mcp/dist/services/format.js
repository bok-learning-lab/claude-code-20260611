/**
 * Shared formatting, pagination, and truncation helpers used by every tool.
 */
import { CHARACTER_LIMIT } from "../constants.js";
/** Output format supported by every data-returning tool. */
export var ResponseFormat;
(function (ResponseFormat) {
    ResponseFormat["MARKDOWN"] = "markdown";
    ResponseFormat["JSON"] = "json";
})(ResponseFormat || (ResponseFormat = {}));
/**
 * Derive consistent pagination metadata from an API `info` block.
 *
 * @param info The `info` block from a list response (may be undefined).
 * @param requestedPage The page the caller asked for, used as a fallback.
 * @param count Number of records actually present in this response.
 */
export function pageMeta(info, requestedPage, count) {
    const total = info?.totalrecords ?? count;
    const pages = info?.pages ?? (count > 0 ? 1 : 0);
    const page = info?.page ?? requestedPage;
    const hasMore = page < pages;
    return {
        total,
        pages,
        page,
        count,
        has_more: hasMore,
        next_page: hasMore ? page + 1 : null,
    };
}
/**
 * Render a list of items to a string, shrinking the item set until the result
 * fits within CHARACTER_LIMIT. The render callback receives the (possibly
 * reduced) items and a `truncated` flag so it can include a clear notice and
 * pagination guidance when data was dropped.
 *
 * @param items All items that could be shown.
 * @param render Builds the output string for a given slice of items.
 */
export function fitToLimit(items, render) {
    const full = render(items, false);
    if (full.length <= CHARACTER_LIMIT || items.length <= 1) {
        return full;
    }
    let count = items.length;
    while (count > 1) {
        count = Math.floor(count / 2);
        const candidate = render(items.slice(0, count), true);
        if (candidate.length <= CHARACTER_LIMIT) {
            return candidate;
        }
    }
    return render(items.slice(0, 1), true);
}
/**
 * Collapse whitespace and clip free text to a maximum length, appending an
 * ellipsis when clipped. Returns null for empty/missing input.
 */
export function truncateText(value, max = 600) {
    if (!value)
        return null;
    const collapsed = value.replace(/\s+/g, " ").trim();
    if (!collapsed)
        return null;
    return collapsed.length > max ? `${collapsed.slice(0, max)}…` : collapsed;
}
/** Strip HTML tags from a string (used to clean rich-text catalogue fields). */
export function stripHtml(value) {
    if (!value)
        return null;
    return value.replace(/<[^>]*>/g, " ").replace(/&nbsp;/g, " ");
}
/** Build a standard MCP text tool result. */
export function toolText(text, isError = false) {
    return {
        content: [{ type: "text", text }],
        ...(isError ? { isError: true } : {}),
    };
}
/** A single line in a markdown bullet list, omitted when the value is empty. */
export function bullet(label, value) {
    if (value === null || value === undefined || value === "")
        return null;
    return `- **${label}**: ${String(value)}`;
}
//# sourceMappingURL=format.js.map