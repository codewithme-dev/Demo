from git import Repo
import os

# ✅ Your existing local repo folder (no new folder will be created)
local_path = "D:/VS-Code/Python/Practices For UI/Text_Animation"

# ✅ Open existing Git repo
repo = Repo(local_path)
print("📁 Opened existing Git repository.")

# ✅ Stage all changes
repo.git.add(all=True)

# ✅ Commit changes
repo.index.commit("Updated code from existing local repo using GitPython")
print("✅ Changes committed.")

# ✅ Push to GitHub
origin = repo.remote(name='origin')
origin.push()
print("✅ Changes pushed to GitHub.")
