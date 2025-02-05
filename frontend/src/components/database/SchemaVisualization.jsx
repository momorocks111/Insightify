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
    Object.entries(schema).forEach(([tableName, tableInfo]) => {
      graphDef += `  ${tableName} {\n`;
      tableInfo.columns.forEach((column) => {
        graphDef += `    ${column.type} ${column.name}\n`;
      });
      graphDef += "  }\n";
    });
    return graphDef;
  };

  return <div ref={mermaidRef} id="schema-diagram"></div>;
};

export default SchemaVisualization;
