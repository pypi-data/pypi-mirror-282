

__author__ = "Irfan Hussain"
__email__ = "ir_hussain@hotmail.com"

class hcv_subgenotyes:
    '''
    The dataset is collect from https://www.uniprot.org/uniprotkb?query=HCV+genotypes+subtypes
    Data Formate: 'Entry Number' 'HCV subtype'
    'Q68713_9HEPC subtype 5a', 'Q68714_9HEPC subtype 5a', 'Q68716_9HEPC subtype 2b', 'Q68718_9HEPC subtype 1b', 
    'Q68719_9HEPC subtype 1b', 'Q68720_9HEPC subtype 1b', 'Q68721_9HEPC subtype 1b', 'Q68722_9HEPC subtype 5a', 
    'Q68723_9HEPC subtype 1b', 'Q68724_9HEPC subtype 5a', 'Q68725_9HEPC subtype 5a', 'Q68726_9HEPC subtype 5a', 
    'Q68728_9HEPC subtype 3a', 'Q68729_9HEPC subtype 3a', 'Q68731_9HEPC subtype 2b', 'Q68735_9HEPC subtype 1b',
    'Q68737_9HEPC subtype 1b', 'Q68738_9HEPC subtype 3a', 'Q81280_9HEPC subtype 1d', 'Q81283_9HEPC subtype 1d', 
    'Q81753_9HEPC subtype 2d', 'Q76VQ7_9HEPC subtype 1b', 'Q76VQ8_9HEPC subtype 1b', 'Q76VQ9_9HEPC subtype 1b', 
    'Q81687_9HEPC subtype 3a', 'Q81688_9HEPC subtype 3a', 'Q81689_9HEPC subtype 3a', 'Q81690_9HEPC subtype 3a', 
    'Q81691_9HEPC subtype 3a', 'Q81692_9HEPC subtype 3a', 'Q81693_9HEPC subtype 3a', 'Q81695_9HEPC subtype 4a', 
    'Q81696_9HEPC subtype 4a', 'Q81697_9HEPC subtype 5a', 'Q81698_9HEPC subtype 5a', 'Q81699_9HEPC subtype 5a', 
    'Q81700_9HEPC subtype 5a', 'Q81701_9HEPC subtype 6a', 'Q81719_9HEPC subtype 1b', 'Q81720_9HEPC subtype 1c', 
    'Q81721_9HEPC subtype 1c', 'Q81722_9HEPC subtype 2a', 'Q81723_9HEPC subtype 2a', 'Q81724_9HEPC subtype 2a', 
    'Q81738_9HEPC subtype 2b', 'Q81739_9HEPC subtype 2b', 'Q81740_9HEPC subtype 2b', 'Q81741_9HEPC subtype 2b', 
    'Q81742_9HEPC subtype 2b', 'Q81743_9HEPC subtype 2c', 'Q81744_9HEPC subtype 2c', 'Q81745_9HEPC subtype 2c', 
    'Q81746_9HEPC subtype 2c'
    
    '''
    
    def __init__(self, file_path):
        self.file_path = file_path
        
        
    def find_subgenotype(self):
        
        subgenotype_list = []

        with open(self.file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('>'):
                    if "subtype" in line:
                        Entry_part = line.split('|')[2]
                        Entry_num = Entry_part.split(' ')[0]   
                        genotype_str_index = line.index("subtype")
                        genotype_str_type = Entry_num +" "+line[genotype_str_index:genotype_str_index+10]
                        subgenotype_list.append(genotype_str_type)
                        
        return subgenotype_list
    
    def view_dic(self, sequences):
        for key, value in sequences.items():
            print(f"{key}: {value}")
    
                        
    def read_fasta(self):
        sequences = {}
        current_seq_name = None
        current_seq = []

        with open(self.file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('>'):
                    if current_seq_name and current_seq:
                        sequences[current_seq_name] = ''.join(current_seq)
                        current_seq = []
                    if "subtype" in line:
                        Entry_part = line.split('|')[2]
                        Entry_num = Entry_part.split(' ')[0]   
                        genotype_str_index = line.index("subtype")
                        genotype_str_type = Entry_num +" "+line[genotype_str_index:genotype_str_index+10]
                        current_seq_name = genotype_str_type
                    else:
                        current_seq_name = None
                else:
                    if current_seq_name:
                        current_seq.append(line)

            if current_seq_name and current_seq:
                sequences[current_seq_name] = ''.join(current_seq)

        return sequences

# file_path = 'hcv_genotypes.fasta'
# obj = hcv_subgenotyes(file_path)
# sequences = obj.read_fasta()
# list_genotypes_view = obj.find_subgenotype()
# obj.view_dic(sequences)
# # print("sequences: ", sequences)
# print("List of genotypes: ", list_genotypes_view)
