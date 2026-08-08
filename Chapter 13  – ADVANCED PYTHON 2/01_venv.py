'''
📘 Virtual Environment (Short Note)

A **Virtual Environment** is an **isolated Python environment** for a single project.

It keeps each project's packages separate, so they don't conflict with other projects.

Why use it?

* ✅ Avoid package version conflicts.
* ✅ Keep projects independent.
* ✅ Used in almost every professional Python project.

 Create a Virtual Environment

```powershell
python -m venv .venv
```

 Activate (Windows PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

 Install a Package

```powershell
pip install requests
```

 Save Installed Packages

```powershell
pip freeze > requirements.txt
```

 Install Packages from `requirements.txt`

```powershell
pip install -r requirements.txt
```

 Deactivate

```powershell
deactivate
```

 📝 One-line Definition

A Virtual Environment is a private Python workspace that stores packages separately for each project.** 🚀
'''