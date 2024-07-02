import os 

def convert_template_to_dataproduct(template_path:str):

    print(os.path.join(os.getcwd(), template_path))

    os.system(f'git clone https://github.com/jupyter-naas/data-product-framework.git')