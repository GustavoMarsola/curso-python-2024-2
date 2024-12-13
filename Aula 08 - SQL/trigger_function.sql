-- Comando para criar a função de atualizar o updated_at
CREATE OR REPLACE FUNCTION atualiza_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Comando para atribuir a função à tabela usuarios
CREATE TRIGGER atualiza_usuario_updated_at
BEFORE UPDATE ON usuarios
FOR EACH ROW
EXECUTE FUNCTION atualiza_updated_at();