import os,sys,random
from typing import TypedDict

sys.path.append(os.getcwd())
import yaml
from langchain_openai import ChatOpenAI
from nlpbridge.text.router import RouterManager, Condition


class NodeCondition(Condition):
    def __call__(self, *args, **kwargs):
        if not random.choice([True, False]):
            return "a1"
        else:
            return "a1"

class SimpleCondition(Condition):
    def __call__(self, node_state: TypedDict) -> str:
        return self.cur_node.name


router_manager = RouterManager()

YAML_PATH = "../nlpbridge/config.yaml"
# YAML_PATH = "../../config.yaml"

with open(YAML_PATH, 'r') as file:
    config = yaml.safe_load(file)
redis = config['redis']
config["redis"]["redis_url"] = f"redis://default:{redis['password']}@{redis['url']}:{redis['port']}/{redis['db']}"
os.environ["CONFIG_PATH"] = YAML_PATH
os.environ["OPENAI_BASE_URL"] = config['chatgpt']['url']
os.environ["OPENAI_API_KEY"] = config['chatgpt']['api_key']

llm = ChatOpenAI()
graph, cfg = router_manager.get_graph(chat_id="100014", llm=llm, router_id=1,condition_cls=SimpleCondition)
state = graph.get_state(config=cfg)
print(f'state:\n{state}')
state_next = state.next
print()
print(f'({state_next[0]}) is current node')

for output in graph.stream(input=None, config=cfg):
    for key, value in output.items():
        print(f"({key})[Response]: {value['response']}\n")

print("[Dialogue ends]\n")


def gen_struct_img():
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    try:
        # Assuming graph.get_graph(xray=True).draw_mermaid_png() returns image data
        image_data = graph.get_graph(xray=True).draw_mermaid_png()

        # Save the image data to a file
        with open('output_image.png', 'wb') as f:
            f.write(image_data)

        # Display the image using matplotlib
        img = mpimg.imread('output_image.png')
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.show()

    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {e}")


gen_struct_img()

