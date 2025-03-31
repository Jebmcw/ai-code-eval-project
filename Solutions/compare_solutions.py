import time
import os
import sys
import matplotlib.pyplot as plt

# Dynamically set project root and add to path
script_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.insert(0, project_root)

# Import solution functions
from Solutions.human_solution_1 import reverse_list as human_reverse
from Solutions.ai_solution_1 import reverse_list as ai_reverse

# === Linked list helper structures ===
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# === Prepare test input ===
test_values = list(range(1000))
linked_list_input = build_linked_list(test_values)

# === Time Human Solution ===
start = time.perf_counter()
human_result = human_reverse(build_linked_list(test_values))
human_time = time.perf_counter() - start

# === Time AI Solution ===
start = time.perf_counter()
ai_result = ai_reverse(build_linked_list(test_values))
ai_time = time.perf_counter() - start

# === Validate correctness ===
outputs_match = linked_list_to_list(human_result) == linked_list_to_list(ai_result)

# === Count lines of code ===
human_path = os.path.join(project_root, 'Solutions', 'human_solution_1.py')
ai_path = os.path.join(project_root, 'Solutions', 'ai_solution_1.py')

human_lines = len(open(human_path).readlines())
ai_lines = len(open(ai_path).readlines())

# === Console summary ===
print(f"✅ Outputs Match: {outputs_match}")
print(f"⏱️  Human Time: {human_time:.6f}s | AI Time: {ai_time:.6f}s")
print(f"📏  Human Lines: {human_lines} | AI Lines: {ai_lines}")

# === Output path for plots ===
output_dir = os.path.join(project_root, 'data')
os.makedirs(output_dir, exist_ok=True)

# === Visualization: Execution Time ===
plt.figure(figsize=(6, 4))
plt.bar(['Human', 'AI'], [human_time, ai_time], color=['blue', 'green'])
plt.title('Execution Time Comparison')
plt.ylabel('Seconds')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'execution_time.png'))
plt.show()

# === Visualization: Code Length ===
plt.figure(figsize=(6, 4))
plt.bar(['Human', 'AI'], [human_lines, ai_lines], color=['blue', 'green'])
plt.title('Code Length Comparison')
plt.ylabel('Line Count')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'code_length.png'))
plt.show()


