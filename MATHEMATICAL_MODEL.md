# Kosvo Spatial Mathematical Model

## Overview

This mathematical model represents the underlying structure of the Kosvo Spatial Framework. It describes spatial relationships between an object and an observer through distance, perspective, direction, and rotational movement.

---

## Variables

Object position:

\[
O(x_o, y_o)
\]

Observer position:

\[
P(x_p, y_p)
\]

---

## 1. Distance Relationship (Beside / Kosvo)

The distance between the observer and the object is calculated as:

\[
d=\sqrt{(x_o-x_p)^2+(y_o-y_p)^2}
\]

If:

\[
d < 5
\]

The observer is classified as **Beside** the object.

If:

\[
d \geq 5
\]

The **Third Perspective** is activated.

---

## 2. Third Perspective Direction

The spatial difference between the observer and object is:

\[
\Delta x=x_o-x_p
\]

\[
\Delta y=y_o-y_p
\]

The larger directional change determines the observation perspective:

- \(\Delta x > 0\) → East
- \(\Delta x < 0\) → West
- \(\Delta y > 0\) → North
- \(\Delta y < 0\) → South

---

## 3. Loom Rotation

The rotational movement around the object is represented by:

\[
x=x_o+r\cos(\theta)
\]

\[
y=y_o+r\sin(\theta)
\]

Where:

- \(r\) = rotation radius
- \(\theta\) = rotation angle

---

## Computational Flow

\[
Input \rightarrow Distance \rightarrow Perspective \rightarrow Direction \rightarrow Loom Rotation
\]

---

## Purpose

This model provides a mathematical representation of the Kosvo Spatial Framework by describing entity separation, external observation, and rotational movement around a reference object.
