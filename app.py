from datetime import date
from pathlib import Path
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

# O banco padrão ficará na pasta principal do projeto.
BASE_DIR = Path(__file__).resolve().parent


def obter_caminho_banco():
    """Retorna o caminho do banco configurado para a aplicação."""
    return app.config.get("DATABASE", BASE_DIR / "vertice.db")


def conectar_banco():
    """Abre uma conexão com o banco SQLite."""
    conexao = sqlite3.connect(obter_caminho_banco())
    conexao.row_factory = sqlite3.Row
    return conexao



def criar_tabela():
    """Cria a tabela de agendamentos, se ainda não existir."""
    with conectar_banco() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS agendamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                servico TEXT NOT NULL,
                data TEXT NOT NULL,
                horario TEXT NOT NULL,
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                UNIQUE (data, horario)
            )
        """)


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/agendamentos")
def listar_agendamentos():
    with conectar_banco() as conexao:
        agendamentos = conexao.execute("""
            SELECT id, cliente, servico, data, horario
            FROM agendamentos
            ORDER BY data, horario
        """).fetchall()

    agendamentos_formatados = []

    for agendamento in agendamentos:
        item = dict(agendamento)
        item["data"] = date.fromisoformat(item["data"]).strftime("%d/%m/%Y")
        agendamentos_formatados.append(item)
    
    return render_template(
        "agenda.html",
        agendamentos=agendamentos_formatados
    )


@app.route("/agendamentos/novo", methods=["GET", "POST"])
def novo_agendamento():
    if request.method == "POST":
        cliente = request.form.get("cliente", "").strip()
        servico = request.form.get("servico", "").strip()
        data = request.form.get("data", "").strip()
        horario = request.form.get("horario", "").strip()

        if not all([cliente, servico, data, horario]):
            return "Erro: preencha todos os campos.", 400

        try:
            # Valida o formato da data e do horário.
            from datetime import date, time

            data_validada = date.fromisoformat(data)
            time.fromisoformat(horario)

            if data_validada < date.today():
                return "Erro: a data não pode estar no passado.", 400

            with conectar_banco() as conexao:
                conexao.execute("""
                    INSERT INTO agendamentos
                        (cliente, servico, data, horario)
                    VALUES (?, ?, ?, ?)
                """, (cliente, servico, data, horario))

            return """
                <h1>Agendamento salvo com sucesso!</h1>
                <p>O registro foi gravado no banco de dados.</p>
                <p><a href="/agendamentos/novo">Novo agendamento</a></p>
                <p><a href="/">Voltar ao menu</a></p>
            """

        except ValueError:
            return "Erro: informe uma data e um horário válidos.", 400

        except sqlite3.IntegrityError:
            return """
                <h1>Horário indisponível</h1>
                <p>Já existe um agendamento nessa data e horário.</p>
                <p><a href="/agendamentos/novo">Tentar outro horário</a></p>
            """, 409

    return render_template("novo_agendamento.html")


# Prepara o banco antes de iniciar o servidor.
criar_tabela()


if __name__ == "__main__":
    app.run(debug=True)
