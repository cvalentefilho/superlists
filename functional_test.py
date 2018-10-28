import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação online insteressante para
        # lista de  tarefas. Ele decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que o título da página e o cabeçalho mencionam listas de
        # tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finsih test!')

        # Ela é convidada a inserir um item de tarefa imediatamente

        # Ela digita "Buy peacock feathers" em uma caixa
        # de texto

        # Quando ela tecla enter, a página é atualizada, e agora a página lista
        # "1: Buy peacock feathers" como um  item em uma lista de tarefas

        # Ainda continua havendo uma caixa de convidando à acrescentar outro
        # item. Ela insere "Use peacock feathers to make a fly"

        # A lista é atualizada novamente e agora mostra os dois itens em sua lista

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota
        # que o site gerou uma URL única para ela -- há um pequeno
        # texto explicativo para isso.

        # Ela acessa essa URL - sua lista de tarefas contnua lá.

        # Satisfeita, ela volta a dormir


if __name__ == '__main__':
    unittest.main(warnings='ignore')
