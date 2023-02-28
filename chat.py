from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create object of ChatBot class with Storage and Logic Adapter
bot = ChatBot('Karty',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  'chatterbot.logic.BestMatch',
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'I am sorry, but I do not understand. I am still learning.',
                      'maximum_similarity_threshold': 0.90
                  }
              ],
              filters=[
                  'chatterbot.filters.RepetitiveResponseFilter'
              ],
              input_adapter='chatterbot.input.TerminalAdapter',
              output_adapter='chatterbot.output.TerminalAdapter',
              database='conversations',
              database_uri='mysql+pymysql://root:IdlP#bxj59@localhost/conversations'
              )

# Training With Own Questions
trainer = ListTrainer(bot)
# Get data from lists
training_data_questions = open('training_data/health_qn.txt').read().splitlines()
training_data_personal = open('training_data/personal_qn.txt').read().splitlines()
training_data = training_data_questions + training_data_personal
trainer.train(training_data)
