from emprestimos import pode_realizar_emprestimo


def test_permite_emprestimo_quando_abaixo_do_limite():
    assert pode_realizar_emprestimo(
        emprestimos_abertos=2,
        limite=3
    ) is True
    def test_bloqueia_quando_atinge_limite():
    assert pode_realizar_emprestimo(3, 3) is False