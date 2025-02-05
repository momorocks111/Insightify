import React, { useEffect, useRef } from "react";
import { useDatabaseContext } from "../../contexts/DatabaseContext";
import mermaid from "mermaid";

const SchemaVisualization = () => {
  const { databaseSchema } = useDatabaseContext();
  const mermaidRef = useRef(null);

  useEffect(() => {
    if (databaseSchema && mermaidRef.current) {
      const graphDefinition = generateMermaidGraph(databaseSchema);
      mermaid.initialize({ startOnLoad: true });
      mermaid.render("schema-diagram", graphDefinition, (svgCode) => {
        mermaidRef.current.innerHTML = svgCode;
      });
    }
  }, [databaseSchema]);

  const generateMermaidGraph = (schema) => {
    let graphDef = "erDiagram\n";
    if (Array.isArray(schema)) {
      // SQL statements
      schema
        .filter((stmt) => stmt.type === "CREATE")
        .forEach((table) => {
          graphDef += `  ${table.table} {\n    ${table.columns}\n  }\n`;
        });
    } else if (schema.tables) {
      // SQLite database
      Object.entries(schema.tables).forEach(([tableName, tableInfo]) => {
        graphDef += `  ${tableName} {\n`;
        Object.entries(tableInfo.dtypes).forEach(([columnName, columnType]) => {
          graphDef += `    ${columnType} ${columnName}\n`;
        });
        graphDef += "  }\n";
      });
    } else {
      // Single table (CSV/Excel)
      graphDef += `  Data {\n`;
      Object.entries(schema.dtypes).forEach(([columnName, columnType]) => {
        graphDef += `    ${columnType} ${columnName}\n`;
      });
      graphDef += "  }\n";
    }
    return graphDef;
  };

  return <div ref={mermaidRef} id="schema-diagram"></div>;
};

export default SchemaVisualization;
