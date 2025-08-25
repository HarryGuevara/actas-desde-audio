def test_imports():
    import src.transcribe as t
    import src.cleaning as c
    import src.generate_docx as g
    assert callable(t.transcribir_audio)
    assert callable(c.limpieza_basica)
    assert callable(g.crear_acta_docx)
