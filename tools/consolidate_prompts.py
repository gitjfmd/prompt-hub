import os
import yaml
import shutil

# Configuration
WORKSPACE_DIR = "/home/ubuntu/full-prompt-hub-workspace"
OUTPUT_DIR = "/home/ubuntu/full-prompt-hub"

# Main function
def main():
    # Process awesome-ai-system-prompts
    process_awesome_ai_system_prompts()

    # Process fabric patterns
    process_fabric_patterns()

    # Process leaked-system-prompts
    process_leaked_system_prompts()

    # Process other repositories (add more functions as needed)

# Function to process awesome-ai-system-prompts
def process_awesome_ai_system_prompts():
    repo_path = os.path.join(WORKSPACE_DIR, "awesome-ai-system-prompts")
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".md"):
                # Extract information from file path
                parts = root.split(os.sep)
                service = parts[-1]
                prompt_name = file.replace(".md", "")

                # Create metadata
                metadata = {
                    "uid": f"{get_date()}-{service.lower()}-{prompt_name.lower().replace(' ', '-')}",
                    "name": f"{service} - {prompt_name}",
                    "description": f"System prompt for {service} - {prompt_name}",
                    "author": "Unknown",
                    "date": get_date(),
                    "service": [service.lower()],
                    "task": ["system-prompt"],
                    "type": ["system-prompt"],
                    "source": [
                        {
                            "name": "awesome-ai-system-prompts",
                            "url": "https://github.com/dontriskit/awesome-ai-system-prompts",
                            "file": os.path.join(root, file).replace(repo_path + "/", "")
                        }
                    ]
                }

                # Read prompt content
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()

                # Write to new file
                write_prompt_file(metadata, content)

# Function to process fabric patterns
def process_fabric_patterns():
    repo_path = os.path.join(WORKSPACE_DIR, "fabric", "data", "patterns")
    for pattern in os.listdir(repo_path):
        pattern_path = os.path.join(repo_path, pattern)
        if os.path.isdir(pattern_path):
            system_file = os.path.join(pattern_path, "system.md")
            if os.path.exists(system_file):
                # Create metadata
                metadata = {
                    "uid": f"{get_date()}-fabric-{pattern.lower()}",
                    "name": f"Fabric Pattern: {pattern}",
                    "description": f"A prompt pattern from the Fabric framework.",
                    "author": "Fabric Community",
                    "date": get_date(),
                    "service": ["fabric"],
                    "task": ["task-prompt"],
                    "type": ["pattern"],
                    "source": [
                        {
                            "name": "fabric",
                            "url": "https://github.com/danielmiessler/fabric",
                            "file": os.path.join(pattern_path, "system.md").replace(os.path.join(WORKSPACE_DIR, "fabric") + "/", "")
                        }
                    ]
                }

                # Read prompt content
                with open(system_file, "r") as f:
                    content = f.read()

                # Write to new file
                write_prompt_file(metadata, content)

# Function to process leaked-system-prompts
def process_leaked_system_prompts():
    repo_path = os.path.join(WORKSPACE_DIR, "leaked-system-prompts")
    for file in os.listdir(repo_path):
        if file.endswith(".md"):
            # Extract information from filename
            parts = file.replace(".md", "").split("_")
            service = parts[0]
            date = parts[1] if len(parts) > 1 else get_date()

            # Create metadata
            metadata = {
                "uid": f"{date}-{service.lower()}-{file.replace('.md', '').lower()}",
                "name": f"{service} Leaked System Prompt ({date})",
                "description": f"Leaked system prompt for {service} from {date}.",
                "author": "Unknown (leaked)",
                "date": date,
                "service": [service.lower()],
                "task": ["system-prompt"],
                "type": ["leaked", "system-prompt"],
                "source": [
                    {
                        "name": "leaked-system-prompts",
                        "url": "https://github.com/jujumilk3/leaked-system-prompts",
                        "file": file
                    }
                ]
            }

            # Read prompt content
            with open(os.path.join(repo_path, file), "r") as f:
                content = f.read()

            # Write to new file
            write_prompt_file(metadata, content)

# Helper function to write prompt file
def write_prompt_file(metadata, content):
    # Create directories
    service_dir = os.path.join(OUTPUT_DIR, "by-service", metadata["service"][0])
    task_dir = os.path.join(OUTPUT_DIR, "by-task", metadata["task"][0])
    type_dir = os.path.join(OUTPUT_DIR, "by-type", metadata["type"][0])
    os.makedirs(service_dir, exist_ok=True)
    os.makedirs(task_dir, exist_ok=True)
    os.makedirs(type_dir, exist_ok=True)

    # Create file content
    file_content = f"---\n{yaml.dump(metadata)}---\n\n{content}"

    # Write to files
    with open(os.path.join(service_dir, f"{metadata['uid']}.md"), "w") as f:
        f.write(file_content)
    with open(os.path.join(task_dir, f"{metadata['uid']}.md"), "w") as f:
        f.write(file_content)
    with open(os.path.join(type_dir, f"{metadata['uid']}.md"), "w") as f:
        f.write(file_content)

# Helper function to get current date
def get_date():
    from datetime import datetime
    return datetime.now().strftime("%Y%m%d")

# Run the script
if __name__ == "__main__":
    main()


