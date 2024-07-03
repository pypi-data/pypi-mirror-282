import git
import os
import shutil


def get_data_file_content(data):

    content = f"""
    import {{PageType, SiteType}} from "@/utils/types";

    export const page1: PageType = {{
        title: "{data['page1']['title']}",
        link: "{data['page1']['link']}",
        headline: "{data['page1']['headline']}",
        description: "{data['page1']['description']}",
        phone_number: "{data['page1']['phone_number']}",
    }}

    export const page2: PageType = {{
        title: "{data['page2']['title']}",
        link: "{data['page2']['link']}",
        headline: "{data['page2']['headline']}",
        description: "{data['page2']['description']}",
        phone_number: "{data['page2']['phone_number']}",
    }}

    export const home_page: PageType = {{
        title: "{data['home_page']['title']}",
        link: "{data['home_page']['link']}",
        headline: "{data['home_page']['headline']}",
        description: "{data['home_page']['description']}",
        phone_number: "{data['home_page']['phone_number']}",
    }}

    export const site: SiteType = {{
        name: "{data['name']}",
        domain: "{data['domain']}",
        bg_color: "{data['bg_color']}",
        text_color: "{data['text_color']}",
        home_page: home_page,
        page1: page1,
        page2: page2,
    }}
    """

    return content


def create_site(template_folder, dest_folder, data):

    home_folder = data["domain"]
    page1_folder = data["page1"]["link"].replace(home_folder, "").replace("/", "")
    page2_folder = data["page2"]["link"].replace(home_folder, "").replace("/", "")

    data_file_content = get_data_file_content(data)

    try:
        temp_dest_folder = home_folder
        shutil.copytree(template_folder, temp_dest_folder)

        subfolder_path = os.path.join(temp_dest_folder, "page1")
        new_subfolder_path = os.path.join(temp_dest_folder, page1_folder)
        os.rename(subfolder_path, new_subfolder_path)

        subfolder_path = os.path.join(temp_dest_folder, "page2")
        new_subfolder_path = os.path.join(temp_dest_folder, page2_folder)
        os.rename(subfolder_path, new_subfolder_path)

        file_to_update = os.path.join(temp_dest_folder, 'data.ts')
        if os.path.exists(file_to_update):
            with open(file_to_update, 'w') as f:
                f.write(data_file_content)

        shutil.move(temp_dest_folder, dest_folder)
    except OSError as e:
        print(f"Error: {e}")


def publish_site(generated_site):
    repo_name = "tarwiiga_sites"
    repo_url = f"https://github.com/tarwiiga/{repo_name}.git"
    git.Git(repo_name).clone(repo_url)

    destination = f"{repo_name}/src/app"
    template = f"{destination}/template"
    create_site(template, destination, generated_site)

    commit_message = f"Deployed {generated_site['name']} to https://sites.tarwiiga.com/{generated_site['domain']}"

    try:
        repo = git.Repo(repo_name)
        repo.git.add(repo.untracked_files)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        shutil.rmtree(repo_name)
        print(f"Pushed to {repo_url}")
        print(commit_message)
    except Exception as e:
        print(f"Error: {e}")

    published_site = generated_site.copy()
    published_site["url"] = f"https://sites.tarwiiga.com/{published_site['domain']}"

    return published_site

