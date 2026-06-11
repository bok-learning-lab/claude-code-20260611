/**
 * Tool for browsing the controlled vocabularies (classification, worktype,
 * medium, technique) that power the object-search filters. Each shares the same
 * { id, name, objectcount } shape, so a single tool serves all four.
 */
import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
export declare function registerTermTools(server: McpServer): void;
//# sourceMappingURL=terms.d.ts.map