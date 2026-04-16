## Notes
1. Collection of the unordered items.
2. Each element in the set must be unique & immutable.

---
## Wrong
```
❗ Why this is WRONG?

Because:

9 == 9.0  → True

👉 Python treats them as SAME in a set
```
## important
```
🧠 Key Rule (Burn this in brain)

👉 Set does NOT care:

int vs float appearance

👉 It cares:

=> value equality (==)
=> hash
```