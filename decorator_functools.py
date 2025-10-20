import functools

def registrar_log(funcao):
    # O decorator @functools.wraps faz o trabalho de copiar os metadados.
    @functools.wraps(funcao) 
    def wrapper(*args, **kwargs):
        print(f"LOG: A preparar para executar a função: {funcao.__name__}")
        
        # Chamada da função original
        resultado = funcao(*args, **kwargs)
        
        print(f"LOG: Função '{funcao.__name__}' executada com sucesso.")
        return resultado
        
    return wrapper

# Exemplo de Uso
@registrar_log
def sacar(valor):
    """Função que simula uma operação de saque no banco."""
    print(f"Sacando R$ {valor}")
    return True

# Teste: O nome está correto!
print(f"Nome da função decorada: {sacar.__name__}") 
print(f"Documentação: {sacar.__doc__}")

sacar(100)