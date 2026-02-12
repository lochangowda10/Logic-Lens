from graphviz import Digraph
import re

def generate_flowchart_from_code(code: str, language: str) -> str:
    """
    Generate a simple flowchart representation from code
    Returns Graphviz DOT source
    """
    
    dot = Digraph(comment='Code Logic Flow')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue')
    
    # Start node
    dot.node('start', 'START', shape='oval', fillcolor='lightgreen')
    
    node_count = 0
    prev_node = 'start'
    
    lines = code.strip().split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        node_id = f'node_{node_count}'
        node_count += 1
        
        # Detect control structures
        if re.match(r'(for|while)\s+', line):
            label = f"Loop: {line[:30]}..."
            dot.node(node_id, label, shape='diamond', fillcolor='#FFE5B4')
        elif re.match(r'if\s+', line):
            label = f"Condition: {line[:30]}..."
            dot.node(node_id, label, shape='diamond', fillcolor='#B4D7FF')
        elif re.match(r'def\s+\w+', line):
            func_name = re.search(r'def\s+(\w+)', line).group(1)
            label = f"Function: {func_name}"
            dot.node(node_id, label, shape='box', fillcolor='#D7FFB4')
        elif 'return' in line:
            label = f"Return: {line[:30]}..."
            dot.node(node_id, label, fillcolor='#FFD7B4')
        else:
            label = line[:40] + ('...' if len(line) > 40 else '')
            dot.node(node_id, label)
        
        dot.edge(prev_node, node_id)
        prev_node = node_id
    
    # End node
    dot.node('end', 'END', shape='oval', fillcolor='lightcoral')
    dot.edge(prev_node, 'end')
    
    return dot.source

def generate_mermaid_flowchart(code: str, language: str) -> str:
    """
    Generate Mermaid.js flowchart syntax (alternative to Graphviz)
    Better for web rendering
    """
    
    mermaid = ["flowchart TD"]
    mermaid.append("    Start([START])")
    
    node_count = 0
    prev_node = "Start"
    
    lines = code.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        node_id = f"N{node_count}"
        node_count += 1
        
        # Escape special characters for Mermaid
        label = line.replace('"', "'")[:40]
        
        if re.match(r'(for|while)\s+', line):
            mermaid.append(f'    {node_id}{{{label}}}')
        elif re.match(r'if\s+', line):
            mermaid.append(f'    {node_id}{{{label}}}')
        elif re.match(r'def\s+\w+', line):
            mermaid.append(f'    {node_id}[{label}]')
        else:
            mermaid.append(f'    {node_id}[{label}]')
        
        mermaid.append(f'    {prev_node} --> {node_id}')
        prev_node = node_id
    
    mermaid.append("    End([END])")
    mermaid.append(f'    {prev_node} --> End')
    
    return '\n'.join(mermaid)
