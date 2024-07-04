# tests/test_openai_client.py

import unittest
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env para os testes
load_dotenv()

from icodeuplay.openai_client import call_completion

class TestOpenAIClient(unittest.TestCase):

 @patch('icodeuplay.openai_client.client')
 def test_call_completion(self, mock_client):
  # Configura o mock para a resposta da API
  mock_response = MagicMock()
  mock_response.choices = [MagicMock(message=MagicMock(content="mocked response"))]
  mock_client.chat.completions.create.return_value = mock_response
  
  prompt = "Escreva uma história curta sobre um gato aventureiro."
  result = call_completion(prompt)

  # Verifica se a função retornou a resposta esperada
  self.assertEqual(result, "mocked response")

  # Verifica se a API foi chamada com os parâmetros corretos
  mock_client.chat.completions.create.assert_called_once_with(
   model='gpt-3.5-turbo',
   messages=[
    {
     'role': 'user',
     'content': prompt,
    }
   ], max_tokens=300
  )

if __name__ == '__main__':
 unittest.main()
