def show_summary(self):
    original_class = self.classification_manual
    new_class = self.classification_computed
    affected_area = self.affected_percentage
    title_md = f"### {original_class} --> {new_class} ({affected_area} %)"
    display(Markdown(title_md))
