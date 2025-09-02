from fpdf import FPDF

# Criar o currículo em formato PDF com o LinkedIn atualizado
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'MATHEUS OLIVEIRA DA SILVA', ln=True, align='C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 102, 204)  # Azul
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Contato
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 8, '''Contagem – Minas Gerais | (31) 97185-0294 | matheus-1409@outlook.com
GitHub: https://github.com/MatheusOliv777
LinkedIn: https://www.linkedin.com/in/matheus-oliveira777''')
pdf.ln(5)
pdf.cell(0, 0, '------------------------------------------------------------', ln=True)
pdf.ln(5)

# Objetivo
pdf.chapter_title('Objetivo')
pdf.chapter_body('''Buscando minha primeira oportunidade como Desenvolvedor Júnior ou Estagiário em Desenvolvimento de Sistemas, visando aplicar meus conhecimentos acadêmicos na prática, aprender com profissionais experientes e contribuir para projetos de tecnologia.''')

# Formação Acadêmica
pdf.chapter_title('Formação Acadêmica')
pdf.chapter_body('''Análise e Desenvolvimento de Sistemas
Centro Universitário Una — Cursando''')

# Certificados
pdf.chapter_title('Certificados')
pdf.chapter_body('''• Ambientes Computacionais e Conectividade — Centro Universitário Una
  Carga horária: 160 horas — Concluído em abril de 2025
  Validação: https://cloudapp.animaeducacao.com.br/validador-documento/?code=82895707a0344a3aaa0fff634c578654

• Formação Discover: Fundamentos Web e Programação — Rocketseat
  Certificado: https://app.rocketseat.com.br/certificates/327e51c2-7429-421a-8876-3d425da49f73''')

# Habilidades Técnicas
pdf.chapter_title('Habilidades Técnicas')
pdf.chapter_body('''• Linguagens: Python, C
• Web: HTML, CSS, JavaScript (básico)
• Controle de Versão: Git e GitHub
• Conceitos: Lógica de Programação, Ambientes Computacionais''')

# Idiomas
pdf.chapter_title('Idiomas')
pdf.chapter_body('''• Inglês — Básico
• Espanhol — Básico''')

# Exportar
pdf_output_path = "/mnt/data/Curriculo_Matheus_Oliveira_atualizado.pdf"
pdf.output(pdf_output_path)
pdf_output_path
