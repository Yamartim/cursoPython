from BrazilData import DocumentoFactory, telefonebrmask, databr, req_api_cep

#cpf = CPF('11111111111')
cpf = DocumentoFactory.geradoc(15316264754)
cnpj = DocumentoFactory.geradoc(91509008000133)

print(cpf, cnpj)

print(telefonebrmask(5511900008888))

print(databr())

print(req_api_cep('01001000'))