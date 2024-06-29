import transaction
from pyramid_celery import celery_app
from caerp.export.task_pdf import ensure_task_pdf_persisted
from caerp_celery.hacks import (
    setup_rendering_hacks,
)
from caerp_celery.mail import (
    send_customer_new_order_mail,
    send_supplier_new_order_mail,
    send_customer_new_invoice_mail,
    send_supplier_new_invoice_mail,
)
from caerp_celery.tasks import utils
from caerp_celery.transactional_task import task_tm
from caerp_celery.conf import get_request

logger = utils.get_logger(__name__)


@task_tm
def scheduled_render_pdf_task(document_id):
    logger.debug("Scheduling a PDF render Task for {}".format(document_id))
    document = utils.get_task(document_id)
    if document is None:
        raise Exception("Document doesn't exist in database")

    request = get_request()
    try:
        # Ensure layout_manager
        setup_rendering_hacks(request, document)
        ensure_task_pdf_persisted(document, request)
        transaction.commit()
    except Exception:
        logger.exception("Error in async_internalestimation_valid_callback")
        transaction.abort()


@task_tm
def async_internalestimation_valid_callback(document_id):
    """
    Handle the transfer of an InternalEstimation to the Client Company

    - Ensure supplier exists
    - Generates the PDF
    - Create a Supplier Order and attache the pdf file
    """
    logger.debug(
        "Async internal estimation validation callback for {}".format(document_id)
    )
    document = utils.get_task(document_id)
    if document is None:
        logger.error(
            "Document with id {} doesn't exist in database".format(document_id)
        )
        return
    else:
        logger.debug("Found the document {}".format(document))
        logger.debug(id(document))

    request = get_request()
    # Ensure layout_manager
    try:
        logger.debug("Setup rendering hacks")
        setup_rendering_hacks(request, document)
        order = document.sync_with_customer(request)
        send_customer_new_order_mail(request, order)
        send_supplier_new_order_mail(request, order)
        transaction.commit()
    except Exception:
        logger.exception("Error in async_internalestimation_valid_callback")
        transaction.abort()


@task_tm
def async_internalinvoice_valid_callback(document_id):
    """
    Handle the transfer of an InternalInvoice to the Client Company

    - Ensure supplier exists
    - Generates the PDF
    - Create a Supplier Invoice and attach the pdf file
    """
    logger.debug(
        "Async internal invoice validation callback for {}".format(document_id)
    )
    document = utils.get_task(document_id)
    if document is None:
        logger.error(
            "Document with id {} doesn't exist in database".format(document_id)
        )
        return

    pyramid_request = get_request()
    # Ensure layout_manager
    try:
        setup_rendering_hacks(pyramid_request, document)
        utils.set_current_user(pyramid_request, document.status_user_id)
        supplier_invoice = document.sync_with_customer(pyramid_request)
        send_customer_new_invoice_mail(pyramid_request, supplier_invoice)
        send_supplier_new_invoice_mail(pyramid_request, supplier_invoice)
        transaction.commit()
    except Exception:
        logger.exception("Error in async_internalinvoice_valid_callback")
        transaction.abort()
