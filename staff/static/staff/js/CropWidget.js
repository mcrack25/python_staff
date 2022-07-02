document.addEventListener("DOMContentLoaded", () => {

    class CropWidget {
        constructor(widget) {
            this.widget = widget;
            this.isVisible = "is-visible";
            this.modalId = 'crop-widget-modal';
        }

        hasModal() {
            console.log('hasModal');
            if (document.getElementById(this.modalId)) {
                return true;
            }
            return false;
        }

        templateModal() {
            console.log('templateModal');
            return `
                <div class="modal crop-widget-modal" id="${this.modalId}">
                    <div class="modal-dialog">
                        <header class="modal-header">
                            The header of the second modal
                            <button class="close-modal" aria-label="close modal" data-close>
                                ✕
                            </button>
                        </header>
                        <section class="modal-content">
                            <p><strong>Press ✕, ESC, or click outside of the modal to close it</strong></p>
                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo repellendus reprehenderit accusamus totam
                                ratione! Nesciunt, nemo dolorum recusandae ad ex nam similique dolorem ab perspiciatis qui. Facere,
                                dignissimos. Nemo, ea.</p>
                            <p>Nullam vitae enim vel diam elementum tincidunt a eget metus. Curabitur finibus vestibulum rutrum.
                                Vestibulum semper tellus vitae tortor condimentum porta. Sed id ex arcu. Vestibulum eleifend tortor non
                                purus porta dapibus</p>
                        </section>
                        <footer class="modal-footer">
                            The footer of the second modal
                        </footer>
                    </div>
                </div>`;
        }

        createModal() {
            console.log('createModal');
            if (!this.hasModal()) {
                document.querySelector('body').insertAdjacentHTML('beforeend', this.templateModal());
            }
        }

        openModal() {
            document.getElementById(this.modalId).classList.add(this.isVisible);
        }

        closeModal() {
            const modal = document.getElementById(this.modalId);
            if (modal.classList.contains(this.isVisible)) {
                modal.classList.remove(this.isVisible);
            };
        }

        clearFileInput() {
            this.widget.querySelector('input').value = null;
        };

        addInputFileListenner() {
            console.log('addInputFileListenner');
            this.widget.querySelector('input[type="file"]').addEventListener("change", e => {
                this.openModal();
            });
        }

        addCloseListenners() {
            console.log('addCloseListenner');

            const modal = document.getElementById(this.modalId);

            // close by button
            modal.querySelector('.close-modal').addEventListener("click", e => {
                e.preventDefault();
                this.closeModal();
                this.clearFileInput();
            });

            // close by keydowwn esc
            document.addEventListener("keyup", e => {
                if (e.key == "Escape" && modal.classList.contains(this.isVisible)) {
                    this.closeModal();
                    this.clearFileInput();
                }
            });

            // close by modal wrapper
            document.addEventListener("click", e => {
                if (e.target == modal && modal.classList.contains(this.isVisible)) {
                    this.closeModal();
                    this.clearFileInput();
                }
            });
        }

        run() {
            console.log('RUN');
            this.createModal();
            this.addInputFileListenner();
            this.addCloseListenners();
        }
    }

    const cropWidgets = document.querySelectorAll('.crop-widget');
    cropWidgets.forEach((cropWidget) => {
        const widget = new CropWidget(cropWidget)
        widget.run();
    });
}, {'once':true})
