export function BlackBackground({onClose}) {
    return (
        <>
            <div className="modal-background" onClick={() => onClose()}>
            </div>
        </>
    )
}