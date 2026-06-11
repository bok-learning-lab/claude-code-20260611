# Lecture 1: Introduction to Algorithms and their Limitations
**CS 1200 | January 26, 2026**

---

## What is an Algorithm?

- Steps to solve a problem
- Procedure given inputs $\to$ outputs
- Simplification of a "real-world way to solve a problem"
- Methodology to manage a data set

---

## Course Structure

| Unit | Topic |
|------|-------|
| 1 | Storing \& Searching |
| 2 | Computational Models |
| 3 | Graph \& Logic |
| 4/5 | Computational Complexity \& Uncomputability |

---

## Unit 1 — Goals

- Abstracting a computational problem
- Prove an algorithm solves a problem
- Analyze and compare efficiency
- Formalize "what is an algorithm"

---

## Motivating Example: Keyword Search on Google

**PageRank:** $\text{PR}(\text{url}) \in [0,1]$ for every url on the WWW

**Keyword search:** Given word $w$, consider $S_w = \{\text{all urls where } w \text{ is found}\}$

**Output:** Sorted list — return urls in $S_w$ in decreasing order of $\text{PR}(\cdot)$

---

## The Sorting Problem

**Input:** $A = \{(K_0, V_0),\ (K_1, V_1),\ \ldots,\ (K_{n-1}, V_{n-1})\}$
where each $K_i \in \mathbb{R}$

**Output:** Array $A' = \{(K_0', V_0'),\ (K_1', V_1'),\ \ldots,\ (K_{n-1}', V_{n-1}')\}$ such that $A'$ is a *valid sort* of $A$:

- $K_0' \leq K_1' \leq \cdots \leq K_{n-1}'$
- $\exists$ permutation $\pi: [n] \to [n]$ such that $(K_i', V_i') = (K_{\pi(i)}, V_{\pi(i)})$

---

## Applying the Sorting Abstraction to Google Search

From $S_w$, define:

$$K_i = 1 - \text{PR}(\text{url}_i), \qquad V_i = \text{url}_i$$

Sorting by $K_i$ gives urls in decreasing order of PageRank.

---

## Insertion Sort

**InsertionSort($A$):**

For all $i = 0$ to $n-1$:

1. Find the smallest $j \leq i$ such that $A[j][0] \geq A[i][0]$
2. Insert $A[i]$ at position $j$ and shift $A[j \ldots i-1]$ to $A[j+1 \ldots i]$

---

## Insertion Sort — Example

**Input:** $(6,a),\ (2,b),\ (1,c),\ (9,d)$

| $i$ | Array state |
|-----|-------------|
| 0 | $(6,a),\ (2,b),\ (1,c),\ (9,d)$ |
| 1 | $(2,b),\ (6,a),\ (1,c),\ (9,d)$ |
| 2 | $(1,c),\ (2,b),\ (6,a),\ (9,d)$ |
| 3 | $(1,c),\ (2,b),\ (6,a),\ (9,d)$ |
