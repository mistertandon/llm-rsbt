Below is a **concise, practical list of commonly used keyboard shortcuts** when working with **JupyterLab inside VS Code** (via the **Jupyter VS Code extension**). This reflects how VS Code actually behaves, not classic browser-based JupyterLab.

---

## 1. Cell execution shortcuts (most important)

| Action                  | Shortcut (Windows / Linux)          | Shortcut (macOS) |
| ----------------------- | ----------------------------------- | ---------------- |
| Run cell                | `Ctrl + Enter`                      | `Cmd + Enter`    |
| Run cell & move to next | `Shift + Enter`                     | `Shift + Enter`  |
| Run cell & insert below | `Alt + Enter`                       | `Option + Enter` |
| Interrupt kernel        | `Ctrl + C` (cell running)           | `Cmd + C`        |
| Restart kernel          | `Ctrl + Shift + P` → Restart Kernel | Same             |

---

## 2. Command Mode vs Edit Mode (critical concept)

| Mode               | Action                      | Shortcut |
| ------------------ | --------------------------- | -------- |
| Enter Edit Mode    | Click cell or press `Enter` |          |
| Enter Command Mode | Press `Esc`                 |          |

---

## 3. Command Mode shortcuts (cell-level operations)

(Press `Esc` first)

| Action             | Shortcut  |
| ------------------ | --------- |
| Add cell above     | `A`       |
| Add cell below     | `B`       |
| Delete cell        | `D` `D`   |
| Copy cell          | `C`       |
| Cut cell           | `X`       |
| Paste cell         | `V`       |
| Move cell up       | `Alt + ↑` |
| Move cell down     | `Alt + ↓` |
| Change to Code     | `Y`       |
| Change to Markdown | `M`       |
| Toggle output      | `O`       |

---

## 4. Edit Mode shortcuts (inside cell)

| Action                             | Shortcut          |
| ---------------------------------- | ----------------- |
| Autocomplete                       | `Tab`             |
| Show signature/help                | `Shift + Tab`     |
| Comment line(s)                    | `Ctrl + /`        |
| Multi-cursor                       | `Alt + Click`     |
| Format cell (if formatter enabled) | `Shift + Alt + F` |

---

## 5. VS Code–specific Jupyter shortcuts

| Action            | Shortcut                               |
| ----------------- | -------------------------------------- |
| Command Palette   | `Ctrl + Shift + P`                     |
| Switch kernel     | `Ctrl + Shift + P` → Select Kernel     |
| Clear all outputs | `Ctrl + Shift + P` → Clear All Outputs |
| Export notebook   | `Ctrl + Shift + P` → Export            |

---

## 6. Notebook navigation

| Action              | Shortcut              |
| ------------------- | --------------------- |
| Focus next cell     | `↓` (Command mode)    |
| Focus previous cell | `↑` (Command mode)    |
| Scroll output       | `Shift + Mouse Wheel` |

---

## 7. View / productivity tips (highly useful)

* Toggle line numbers:
  **Command Palette → “Notebook: Toggle Line Numbers”**
* Collapse outputs:
  Click output header or use `O`
* Disable variable auto-display (important for you):
  End cell with `;`

---

## 8. Customize shortcuts (recommended)

You can customize all Jupyter shortcuts:

```text
Ctrl + Shift + P → Preferences: Open Keyboard Shortcuts
Search: "notebook"
```
---