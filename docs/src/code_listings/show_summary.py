def show_summary(self):
    original_class = self.classification_manual
    new_class = self.classification_computed
    title_md = f"### {original_class} --> " \
                "{new_class} ({self.affected_percentage} %)"
    display(Markdown(title_md))
