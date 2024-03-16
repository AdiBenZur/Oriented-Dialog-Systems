import json
from compare_clustering_solutions import evaluate_clustering
from sentence_transformers import SentenceTransformer


def analyze_unrecognized_requests(data_file, output_file, min_size):
    # todo: implement this function
    #  you are encouraged to break the functionality into multiple functions,
    #  but don't split your code into multiple *.py files
    #
    #  todo: the final outcome is the json file with clustering results saved as output_file

    with open(data_file, 'r') as file:
        clusters = []  # Initialize to empty, will contain all the cluster's name
        dist_matrix = []
        sentences = []
        change_occurred = True

        # Remove numbers from sentences
        for line in file:
            sentence = line.split(',', 1)[1].strip()
            sentences.append(sentence)

        model = SentenceTransformer("all-MiniLM-L6-v2")

        # Sentences are encoded by calling model.encode()
        embeddings = model.encode(sentences)

        # Print the embeddings
        for sentence, embedding in zip(sentences, embeddings):
            print("Sentence:", sentence)
            print("Embedding:", embedding)
            print("")


        while not change_occurred:
            change_occurred = False

            # Iterate over the sentences and map to clusters



if __name__ == '__main__':
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)

    analyze_unrecognized_requests(config['data_file'],
                                  config['output_file'],
                                  config['min_cluster_size'])

    # todo: evaluate your clustering solution against the provided one
    evaluate_clustering(config['example_solution_file'], config['example_solution_file'])  # invocation example
    #evaluate_clustering(config['example_solution_file'], config['output_file'])
