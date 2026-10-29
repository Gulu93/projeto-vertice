
import pytest

from app import app, criar_tabela


@pytest.fixture
def cliente_teste(tmp_path):
    # Cria um banco SQLite exclusivo para este teste.
    banco_teste = tmp_path / "teste_vertice.db"

    # Configura a aplicação para usar o banco isolado.
    app.config["DATABASE"] = banco_teste

    # Cria as tabelas no banco de teste.
    criar_tabela()

    # Cria um cliente para simular requisições HTTP.
    with app.test_client() as cliente:
        yield cliente

    # Limpa a configuração ao terminar.
    app.config.pop("DATABASE", None)


def test_pagina_inicial(cliente_teste):
    resposta = cliente_teste.get("/")

    assert resposta.status_code == 200
    assert b"Projeto V\xc3\xa9rtice" in resposta.data


def test_cadastrar_agendamento(cliente_teste):
    resposta = cliente_teste.post(
        "/agendamentos/novo",
        data={
            "cliente": "Cliente de Teste",
            "servico": "Corte de cabelo",
            "data": "2099-12-15",
            "horario": "10:30",
        },
    )

    assert resposta.status_code == 200
    assert b"Agendamento salvo com sucesso!" in resposta.data

    # Confirma que o registro aparece na agenda.
    resposta_agenda = cliente_teste.get("/agendamentos")

    assert resposta_agenda.status_code == 200
    assert b"Cliente de Teste" in resposta_agenda.data
    assert b"Corte de cabelo" in resposta_agenda.data


def test_impedir_agendamento_duplicado(cliente_teste):
    dados = {
        "cliente": "Cliente A",
        "servico": "Corte de cabelo",
        "data": "2099-12-15",
        "horario": "10:30",
    }

    primeira_resposta = cliente_teste.post(
        "/agendamentos/novo",
        data=dados,
    )

    segunda_resposta = cliente_teste.post(
        "/agendamentos/novo",
        data={
            **dados,
            "cliente": "Cliente B",
        },
    )

    assert primeira_resposta.status_code == 200
    assert segunda_resposta.status_code == 409
    assert b"Hor\xc3\xa1rio indispon\xc3\xadvel" in segunda_resposta.data


def test_rejeitar_campos_vazios(cliente_teste):
    resposta = cliente_teste.post(
        "/agendamentos/novo",
        data={
            "cliente": "",
            "servico": "Corte de cabelo",
            "data": "2099-12-15",
            "horario": "10:30",
        },
    )

    assert resposta.status_code == 400
    assert b"preencha todos os campos" in resposta.data


def test_rejeitar_data_no_passado(cliente_teste):
    resposta = cliente_teste.post(
        "/agendamentos/novo",
        data={
            "cliente": "Cliente de Teste",
            "servico": "Corte de cabelo",
            "data": "2000-01-01",
            "horario": "10:30",
        },
    )

    assert resposta.status_code == 400
    assert b"data n\xc3\xa3o pode estar no passado" in resposta.data
