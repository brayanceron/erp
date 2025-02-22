import { HSOverlay } from "flyonui/flyonui"

type ModalProps = { title?: string, message: string, id: string, size?: string, vertical?: string, horizontal?: string }

export function ModalComponent({ title = "Title", message, id, size = '', vertical = 'middle', horizontal = 'center' }: ModalProps) {

    size = ['sm', 'lg', 'xlg'].includes(size) ? "modal-dialog-" + size : ''
    horizontal = ['start', 'end'].includes(horizontal) ? '-' + horizontal : ''
    vertical = ['top', 'middle', 'bottom'].includes(vertical) ? vertical : 'middle'

    const position = 'modal-'+vertical+horizontal

    console.log(position);

    return (

        // <div id={id} className={`overlay modal overlay-open:opacity-100 modal-middle-end hidden`} role="dialog" > 
        <div id={id} className={"overlay modal overlay-open:opacity-100 " + position + " hidden"} role="dialog" >
            <div className={"modal-dialog overlay-open:opacity-100 " + size}>
                <div className="modal-content">
                    <div className="modal-header">
                        <h3 className="modal-title">{title}</h3>
                        <button type="button" className="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay={"#" + id}>
                            <span className="icon-[tabler--x] size-4"></span>
                        </button>
                    </div>
                    <div className="modal-body">
                        {message}
                    </div>
                    <div className="modal-footer">
                        {/* <button type="button" className="btn btn-soft btn-secondary" data-overlay="#middle-center-modal">Close</button> */}
                        <button type="button" className="btn btn-soft btn-secondary" data-overlay={"#" + id}>Close</button>
                        <button type="button" className="btn bg-black hover:bg-black text-white">Accept</button>
                    </div>
                </div>
            </div>
        </div>


    )

}

export function openModal(event: any, id: string) {
    event
    HSOverlay.open(`#${id}`)
    // let idd  = document.querySelector('#'+id) 
    // const h = document.createElement('a')
    // if(!idd) return
    // modal.open()
}
export function closeModal(event: any, id: string) {
    event
    HSOverlay.close(`#${id}`)
}