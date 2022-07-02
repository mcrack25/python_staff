document.addEventListener("DOMContentLoaded", () => {

    class CropWidget {
        constructor(widget) {
            this.widget = widget;
            this.isVisible = "is-visible";
            this.modalId = 'crop-widget-modal';
        }

        getModal() {
            return document.getElementById(this.modalId);
        }

        hasModal() {
            console.log('hasModal');
            if (this.getModal()) {
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
                            <img src="" class="crop-widget-modal__img">
                        </section>
                        <footer class="modal-footer">
                            <div class="btn-group pull-left" role="group">
                                <button type="button" class="btn btn-default js-zoom-in">
                                    <span class="glyphicon glyphicon-zoom-in"></span>
                                </button>
                                <button type="button" class="btn btn-default js-zoom-out">
                                    <span class="glyphicon glyphicon-zoom-out"></span>
                                </button>
                            </div>
                            <button type="button" class="btn btn-default" data-dismiss="modal">Nevermind</button>
                            <button type="button" class="btn btn-primary js-crop-and-upload">Crop and upload</button>
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
            this.addImgToModal();
            this.getModal().classList.add(this.isVisible);
        }

        closeModal() {
            if (this.getModal().classList.contains(this.isVisible)) {
                this.getModal().classList.remove(this.isVisible);
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

            const modal = this.getModal();

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

        addImgToModal() {
            const modal = this.getModal();
            const fileImage = this.widget.querySelector('input[type=file]').files[0];
            const reader  = new FileReader();
            reader.readAsDataURL(fileImage);
            reader.onloadend = function () {
                modal.querySelector('.crop-widget-modal__img').src = reader.result;
            }
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
