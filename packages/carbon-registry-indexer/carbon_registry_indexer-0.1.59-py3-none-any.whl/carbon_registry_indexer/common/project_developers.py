import os

from carbon_registry_indexer.integrations import utils
from carbon_registry_indexer.models import target

import pandas as pd

def update_project_developers(df, data_dir, project_developer_file_path, projects_file_path):
    # load projects
    target_csv_path = os.path.join(data_dir, project_developer_file_path + ".csv")
    projects_file_path = os.path.join(data_dir, projects_file_path + ".csv")
    projects = pd.read_csv(projects_file_path)

    schema = target.ProjectDeveloper.__table__.columns.keys()

    # generate project developer ids based on name
    df['project_developer_id'] = df.apply(
        lambda row: utils.generate_uuid_from_row(row, ['project_developer_name']), 
        axis=1
    )
    

    for index, row in projects.iterrows():
        filter_condition = df['project_developer_name'] == row['project_developer']
        filtered_rows = df.loc[filter_condition, 'project_developer_id']

        if not filtered_rows.empty:
            projects.at[index, 'project_developer_id'] = filtered_rows.values[0]
            print(f"Updated Project Developer {row['project_developer']}")
        else:
            print(f"No matching project developer found for {row['project_developer']}")

    utils.update_csv(projects, projects_file_path)
    print(f"Processed {len(projects)} projects. Data saved to {projects_file_path}.")

    existing_columns = [col for col in schema if col in df.columns]
    df = df[existing_columns]
    
    # save df
    utils.update_csv(df, target_csv_path, check_schema=False)
    print(f"Processed {len(df)} project developers. Data saved to {target_csv_path}.")
