default persistent.cozy_memorias = []

define cozy_memorias = {
    "bosque": ("Um novo começo", "Fern parou para admirar as cores do bosque na primavera."),
    "caelum": ("Companhia no bosque", "Caelum compartilhou com Fern sua admiração pelas cores da floresta."),
    "rowan": ("Luz entre as árvores", "Rowan observou a luz do sol passando pelas copas.")
}

init python:
    def cozy_registrar_memoria(chave):
        if chave not in cozy_memorias or chave in persistent.cozy_memorias:
            return
        persistent.cozy_memorias = persistent.cozy_memorias + [chave]
        renpy.save_persistent()
        renpy.notify("Memória desbloqueada: " + cozy_memorias[chave][0])

screen cozy_livro():
    tag menu

    $ total = sum(chave in persistent.cozy_memorias for chave in cozy_memorias)
    $ maximo = len(cozy_memorias)

    use game_menu(_("Livro de memórias"), scroll="viewport"):
        vbox:
            spacing 24
            add Transform("images/ui/Memorybook_ICON.png", xysize=(72, 72))
            text _("[total] de [maximo] memórias desbloqueadas"):
                size 34
            for chave, (titulo, descricao) in cozy_memorias.items():
                frame:
                    xfill True
                    padding (24, 20)
                    vbox:
                        spacing 8
                        if chave in persistent.cozy_memorias:
                            text titulo size 32
                            text descricao size 25
                        else:
                            text _("Memória bloqueada") size 32
                            text _("Continue a história para descobrir esta lembrança.") size 25
