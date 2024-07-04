from django.contrib.auth import get_user_model
from django.db import models

from shipdan_model.app_model.constant import FOOD_PRODUCT_ORDER_LIMIT_REQUEST_STATUS, \
    FoodProductOrderLimitRequestStatus, LIMIT_TYPE, LimitType
from shipdan_model.app_model.food import (
    FoodBrand, FoodGroup, FoodProductOrigin, ThirdCategory, StorageMethod, ProductExceptDay, Unit,
    FoodSubSearchCategory, FoodSubClassification, FoodCompany,
)

User = get_user_model()


class OperationProfile(models.Model):
    SHIPDAN_OWNER = 1
    SHIPDAN_MEMBER = 2
    SELLER_OWNER = 3
    SELLER_MEMBER = 4

    AUTHORITIES = (
        (SHIPDAN_OWNER, 'shipdan_owner'),
        (SHIPDAN_MEMBER, 'shipdan_member'),
        (SELLER_OWNER, 'seller_owner'),
        (SELLER_MEMBER, 'seller_member'),
    )

    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, related_name='operation_profile',
        null=True
    )
    company = models.ForeignKey(
        'app_model.FoodCompany', on_delete=models.SET_NULL, related_name='operators', null=True, blank=True
    )
    name = models.CharField(max_length=10, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    contact_email = models.EmailField(max_length=254, blank=True, default='', help_text='실제 연락 받을 이메일입니다.')
    authority = models.IntegerField(choices=AUTHORITIES)

    class Meta:
        db_table = 'oms_operationprofile'


class OperationCompanyInfo(models.Model):
    company = models.OneToOneField(
        'app_model.FoodCompany', on_delete=models.SET_NULL, related_name='company_info',
        null=True
    )
    email_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'oms_operationcompanyinfo'


class FoodProductChangeRequest(models.Model):
    REQUEST_CREATE = 0  # 요청 청사진 생성
    REQUEST_PENDING = 1  # 승인대기
    REQUEST_REJECT = 2  # 요청반려
    REQUEST_COMPLETE = 3  # 승인완료
    REQUEST_CANCEL = 4  # 요청취소

    REQUEST_STATUS = (
        (REQUEST_CREATE, '요청생성'),
        (REQUEST_PENDING, '승인대기'),
        (REQUEST_REJECT, '요청반려'),
        (REQUEST_COMPLETE, '승인완료'),
        (REQUEST_CANCEL, '요청취소'),
    )

    food_product = models.ForeignKey(
        'app_model.FoodProduct', on_delete=models.SET_NULL, related_name='change_requests',
        null=True
    )
    status = models.IntegerField(choices=REQUEST_STATUS)
    requester = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='change_requests_from',
        null=True
    )
    approver = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='change_requests_to',
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_foodproductchangerequest'


class FoodProductChangeRequestContent(models.Model):
    change_request = models.OneToOneField(FoodProductChangeRequest, on_delete=models.CASCADE, related_name='content')

    # food product information
    sku = models.CharField(max_length=20, help_text='재고관리코드', null=True, default=None)
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(FoodBrand, null=True, blank=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(FoodGroup, blank=True, to_field='code', default=FoodGroup.UNDEFINED,
                              on_delete=models.SET_DEFAULT)
    platform = models.ForeignKey(FoodProductOrigin, on_delete=models.CASCADE, null=True, blank=True)
    third_category = models.ForeignKey(ThirdCategory, null=True, blank=True, on_delete=models.CASCADE)
    serving_per_product = models.IntegerField(null=True, help_text='제품당 제공 횟수')
    total_gram = models.FloatField(help_text='총 g', null=True, blank=True)
    unit_gram = models.FloatField(null=True, help_text='단위 그람 수')
    gram_unit = models.IntegerField(choices=Unit.GRAM_UNIT_TYPE, default=Unit.GRAM, help_text='g, ml')
    link = models.URLField(max_length=400, null=True)
    storage_method = models.ForeignKey(StorageMethod, on_delete=models.SET_NULL, null=True, default=None)

    # foreign key
    except_days = models.ManyToManyField(ProductExceptDay, )
    allergies = models.ManyToManyField('app_model.Allergy', )
    sub_search_categories = models.ManyToManyField(FoodSubSearchCategory, )
    sub_classifications = models.ManyToManyField(FoodSubClassification, )

    class Meta:
        db_table = 'oms_foodproductchangerequestcontent'


def change_request_image_path(instance, filename):
    return 'spark/oms/change_request/{}/{}'.format(instance.product.name, filename)


class FoodProductChangeRequestImage(models.Model):
    image = models.ImageField(upload_to=change_request_image_path, null=True)
    product = models.ForeignKey(FoodProductChangeRequestContent, on_delete=models.CASCADE, related_name='images')
    code = models.IntegerField(default=100)

    class Meta:
        db_table = 'oms_foodproductchangerequestimage'


class FoodProductChangeRequestNutrient(models.Model):
    proper_gram = models.FloatField(null=True, help_text='적정 그람 수')
    calorie = models.FloatField(help_text='칼로리(kcal)', null=True, blank=True)
    carbohydrate = models.FloatField(help_text='탄수화물(g)', null=True, blank=True)
    protein = models.FloatField(help_text='단백질(g)', null=True, blank=True)
    fat = models.FloatField(help_text='지방(g)', null=True, blank=True)
    sugar = models.FloatField(help_text='당분(g)', null=True, blank=True)
    sodium = models.FloatField(help_text='나트륨(mg)', null=True, blank=True)
    fiber = models.FloatField(help_text='섬유소(g)', null=True, blank=True)
    saturated_fat = models.FloatField(help_text='포화지방(g)', null=True, blank=True)
    trans_fat = models.FloatField(help_text='트랜스지방(g)', null=True, blank=True)
    cholesterol = models.FloatField(help_text='콜레스테롤(g)', null=True, blank=True)

    content = models.OneToOneField(FoodProductChangeRequestContent, on_delete=models.CASCADE, related_name='nutrient')

    class Meta:
        db_table = 'oms_foodproductchangerequestnutrient'


def order_sheet_path(instance, filename):
    return 'operation/order_sheet/{}.xlsx'.format(filename)


class FoodOrderSheet(models.Model):
    order_sheet = models.FileField(upload_to=order_sheet_path, null=True)
    started_at = models.DateTimeField(null=True)
    ended_at = models.DateTimeField(null=True)
    request_shipping_date = models.DateField(null=True)

    class Meta:
        db_table = 'oms_foodordersheet'


def purchase_order_path(instance, filename):
    return 'operation/purchase_order/{}.zip'.format(filename)


class FoodPurchaseOrderSheet(models.Model):
    purchase_order = models.FileField(upload_to=purchase_order_path, null=True)
    company = models.ForeignKey(FoodCompany, on_delete=models.CASCADE, related_name='purchase_order_sheets', null=True)
    started_at = models.DateTimeField(null=True)
    ended_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'oms_foodpurchaseordersheet'


class SupplyCompany(models.Model):
    """
    사방넷 : deprecated
    """
    name = models.CharField(max_length=60, help_text='공급사명')
    code = models.CharField(max_length=20, help_text='공급사 코드')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_supplycompany'


class ShippingProduct(models.Model):
    """
    사방넷 : deprecated
    """
    product_id = models.IntegerField(unique=True, null=True, help_text='사방넷 shipping_product id')
    name = models.CharField(max_length=100, help_text='product_name', unique=True)
    code = models.CharField(max_length=20, help_text='product_code', unique=True)

    upc = models.CharField(max_length=50, help_text='대표 바코드', null=True, blank=True)
    manage_code1 = models.CharField(max_length=30, help_text='관리키워드1', null=True, blank=True)
    manage_code2 = models.CharField(max_length=30, help_text='관리키워드2', null=True, blank=True)
    manage_code3 = models.CharField(max_length=30, help_text='관리키워드3', null=True, blank=True)
    description = models.CharField(max_length=250, help_text='상품 설명', null=True, blank=True)

    single_width = models.IntegerField(help_text='낱개-가로(mm)', null=True)
    single_length = models.IntegerField(help_text='낱개-세로(mm)', null=True)
    single_height = models.IntegerField(help_text='낱개-높이(mm)', null=True)

    box_width = models.IntegerField(help_text='카톤박스-가로(mm)', null=True)
    box_length = models.IntegerField(help_text='카톤박스-세로(mm)', null=True)
    box_height = models.IntegerField(help_text='카톤박스-높이(mm)', null=True)
    box_weight = models.IntegerField(help_text='카톤박스-무게(g)', null=True)

    single_eta = models.IntegerField(help_text='카톤박스-낱개입수', null=True)
    palet_count = models.IntegerField(help_text='팔레트 입수', null=True)

    use_expire_date = models.BooleanField(help_text='유통기한 사용 여부', null=True, default=False)  # 사방넷(int) 1: 사용, 0: 사용 안함
    use_make_date = models.BooleanField(help_text='제조일자 사용 여부', null=True, default=False)  # 사방넷(int) 1: 사용, 0: 사용 안함
    expire_date_by_make_date = models.IntegerField(help_text='제조일로부터 일수', null=True)

    warning_expire_date = models.IntegerField(help_text='임박재고 전환 기준일', null=True)
    restricted_expire_date = models.IntegerField(help_text='출고불가 기준일', null=True)

    edit_code = models.CharField(max_length=20, help_text='출고편집코드', null=True)
    max_quantity_per_box = models.IntegerField(help_text='최대합포장 수량', null=True)

    status = models.BooleanField(help_text='활성화 여부', default=True, null=True)  # 사방넷(int) 1: 활성화, 0: 비활성화

    supply_company = models.ForeignKey(SupplyCompany, on_delete=models.SET_NULL, null=True,
                                       related_name='shipping_products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_shippingproduct'


class ShippingProductBarcode(models.Model):
    """
    사방넷 : deprecated
    """
    barcode = models.CharField(max_length=100, help_text='바코드')
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(ShippingProduct, null=True, related_name='barcodes', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_shippingproductbarcode'


class SalesProduct(models.Model):
    """
    사방넷 : deprecated
    """
    product_id = models.IntegerField(unique=True, null=True, help_text='사방넷 sales_product id')
    name = models.CharField(max_length=100, help_text='판매상품명', unique=True)
    code = models.CharField(max_length=100, help_text='고유코드', unique=True)

    manage_code1 = models.CharField(max_length=30, help_text='관리키워드1', null=True, blank=True)
    manage_code2 = models.CharField(max_length=30, help_text='관리키워드2', null=True, blank=True)
    manage_code3 = models.CharField(max_length=30, help_text='관리키워드3', null=True, blank=True)
    description = models.CharField(max_length=255, help_text='상품 설명', null=True, blank=True)

    status = models.BooleanField(help_text='활성화 여부', null=True, default=True)  # 사방넷(int) 1: 활성화, 0: 비활성화

    use_display_period = models.BooleanField(help_text='유효기간 사용 여부', null=True,
                                             default=True)  # 사방넷(int) 1: 사용, 0: 사용 안함
    start_dt = models.CharField(max_length=8, help_text='유효기간 시작일 (YYYYMMDD)', null=True)
    end_dt = models.CharField(max_length=8, help_text='유효기간 종료일 (YYYYMMDD)', null=True)

    food_product = models.ForeignKey('app_model.FoodProduct', related_name='sales_products', on_delete=models.SET_NULL,
                                     null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_salesproduct'


class SalesProductShippingProductRelation(models.Model):
    """
    사방넷 : deprecated
    """
    sales_product = models.ForeignKey(SalesProduct, related_name='shipping_product_rels', on_delete=models.CASCADE)
    shipping_product = models.ForeignKey(ShippingProduct, related_name='sales_product_rels', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'oms_salesproductshippingproductrelation'


class OrderReleaseOrderInformation(models.Model):
    """
    사방넷 : deprecated
    """
    """ 쉽단 Order와 사방넷 발주 app_model Relation """

    order = models.OneToOneField('app_model.Order', related_name='release_order_info', on_delete=models.CASCADE)

    is_canceled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_orderreleaseorderinformation'


class ReleaseOrder(models.Model):
    """
    사방넷 : deprecated
    """
    UNDEFINED = 0
    PARCEL = 1
    DIRECT_DELIVERY = 2
    EARLY_MORNING_DELIVERY = 3
    OVERNIGHT_DELIVERY = 4

    SHIPPING_METHOD = (
        (UNDEFINED, '미정'),
        (PARCEL, '택배'),
        (DIRECT_DELIVERY, '직송'),
        (EARLY_MORNING_DELIVERY, '새벽배송'),
        (OVERNIGHT_DELIVERY, '당일배송'),
    )

    BEFORE_RELEASE_REQUEST = 1
    RELEASE_REQUEST = 2
    INVOICE_REGISTER_COMPLETE = 3
    RELEASE_COMPLETE = 4
    RELEASE_CANCEL = 5

    ORDER_STATUS = (
        (UNDEFINED, '미정'),
        (BEFORE_RELEASE_REQUEST, '출고 요청 전'),
        (RELEASE_REQUEST, '출고 요청'),
        (INVOICE_REGISTER_COMPLETE, '송장 등록 완료'),
        (RELEASE_COMPLETE, '출고 완료'),
        (RELEASE_CANCEL, '출고 취소'),
    )

    order_code = models.CharField(max_length=20, null=True, default=None, help_text='오더 코드')
    company_order_code = models.CharField(max_length=100, help_text='주문번호')  # API로 등록하는 경우 unique=True
    shipping_method = models.IntegerField(choices=SHIPPING_METHOD, default=EARLY_MORNING_DELIVERY)
    order_status = models.IntegerField(choices=ORDER_STATUS, default=BEFORE_RELEASE_REQUEST)
    order_date = models.DateTimeField(auto_created=True, null=True, help_text='발주 등록 일시')  # 추가
    request_shipping_dt = models.CharField(max_length=8, help_text='출고 희망일 (YYYYMMDD), 과거 날짜 불가')
    buyer_name = models.CharField(max_length=100, help_text='주문자명', null=True, default='마이쉽단')
    receiver_name = models.CharField(max_length=100, help_text='받는분 이름')
    tel1 = models.CharField(max_length=20, help_text='받는분 전화번호1')
    tel2 = models.CharField(max_length=20, help_text='받는분 전화번호2', null=True)
    zipcode = models.CharField(max_length=20, help_text='받는분 우편번호', null=True)
    shipping_address1 = models.CharField(max_length=150, help_text='받는분 주소1')
    shipping_address2 = models.CharField(max_length=150, help_text='받는분 주소2', null=True)
    shipping_message = models.CharField(max_length=150, help_text='배송메세지', null=True)
    channel_id = models.IntegerField(help_text='발주 타입 id', null=True)
    memo1 = models.CharField(max_length=500, help_text='관리메모1')
    memo2 = models.CharField(max_length=500, help_text='관리메모2')
    memo3 = models.CharField(max_length=500, help_text='관리메모3')
    memo4 = models.CharField(max_length=500, help_text='관리메모4')
    memo5 = models.CharField(max_length=500, help_text='관리메모5')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order_info = models.ForeignKey(OrderReleaseOrderInformation, related_name='release_orders',
                                   null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'oms_releaseorder'


class ReleaseOrderItem(models.Model):
    """
    사방넷 : deprecated
    """
    sales_product = models.ForeignKey(SalesProduct, on_delete=models.SET_NULL, null=True, help_text='판매 상품')
    quantity = models.IntegerField(default=1)

    item_cd1 = models.CharField(max_length=50, null=True, blank=True, help_text='상품별 메모1')
    item_cd2 = models.CharField(max_length=50, null=True, blank=True, help_text='상품별 메모2')
    item_cd3 = models.CharField(max_length=50, null=True, blank=True, help_text='상품별 메모3')

    release_order = models.ForeignKey(ReleaseOrder, on_delete=models.CASCADE, related_name='order_items')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_releaseorderitem'


class FoodProductOrderLimit(models.Model):
    """ start와 end 사이의 주문에 대해서 결제된 식품 수량과 제한 수량 지정 """
    food_product = models.ForeignKey('app_model.FoodProduct', related_name='order_limits', on_delete=models.CASCADE)
    is_available = models.BooleanField(
        help_text='팔리는 날짜 별로 is_available 처리', default=True
    )
    rotation_day = models.IntegerField(null=True, default=None, help_text='for rotation limit')
    limit = models.IntegerField(null=True, default=None)
    ordered_count = models.IntegerField(default=0, help_text='start, end 사이에 결제된 식품 수량')

    start_at = models.DateTimeField(help_text='유저 주문 수량 적용 시점(start)', db_index=True)
    end_at = models.DateTimeField(help_text='유저 주문 수량 적용 시점(end)')

    manufactured_at = models.DateTimeField(
        help_text='생산날짜입니다. limit타입이 rotation인 경우에만 있습니다.',
        null=True, default=None
    )
    validated_at = models.DateTimeField(
        help_text='해당 상품의 유통기한입니다. 생산날짜와 FoodProductStock의 expiration_day로 자동으로 계산되어 기입됩니다.',
        null=True,
        default=None
    )

    # deprecated 3.12.4
    apply_at = models.DateTimeField(help_text='deprecated 되었습니다.', null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_foodproductorderlimit'
        constraints = [
            models.UniqueConstraint(fields=['food_product', 'start_at'], name='FoodProductOrderLimit food_product start_at unique')
        ]

    def __str__(self):
        return f'{self.id}_{self.food_product.name}'


class FoodProductOrderLimitRequest(models.Model):
    """
    주문 수량 제한 수정 요청
    [3.12.4] deprecated : FoodProductOrderLimit를
    """

    limit = models.ForeignKey(FoodProductOrderLimit, related_name='requests', on_delete=models.CASCADE)
    status = models.IntegerField(choices=FOOD_PRODUCT_ORDER_LIMIT_REQUEST_STATUS,
                                 default=FoodProductOrderLimitRequestStatus.UNDEFINED)
    amount = models.IntegerField(null=True, default=None, help_text='적용될 주문 제한 수량')

    apply_at = models.DateTimeField(help_text='적용 시점')
    start_at = models.DateTimeField(help_text='유저 주문 수량 적용 시점(start)')
    end_at = models.DateTimeField(help_text='유저 주문 수량 적용 시점(end)')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_foodproductorderlimitrequest'
        constraints = [
            models.UniqueConstraint(fields=['limit', 'apply_at'],
                                    name='unique limit and status for FoodProductOrderLimitRequest')
        ]


class FoodProductOrderLimitRequestLog(models.Model):
    """
    주문 수량 제한 수정 요청 로그
    [3.12.4] deprecated : FoodProductOrderLimit를 장고 어드민에서 관리하게 되어, 따로 로그 시스템이 필요없게 됨.
    변화점은 장고 어드민의 값으로 처리
    """
    request = models.ForeignKey(FoodProductOrderLimitRequest, related_name='logs', on_delete=models.CASCADE)
    log_type = models.IntegerField(choices=FOOD_PRODUCT_ORDER_LIMIT_REQUEST_STATUS,
                                   default=FoodProductOrderLimitRequestStatus.UNDEFINED)

    amount = models.IntegerField(null=True, default=None, help_text='적용될 주문 제한 수량')
    start_at = models.DateTimeField(help_text='유저 주문 수량 적용 시점(start)')
    end_at = models.DateTimeField(help_text='유저 주문 수량 적용 시점(end)')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_foodproductorderlimitrequestlog'


class FoodProductPurchaseLog(models.Model):
    """ 식품 결제, 결제 취소에 대한 로그 """

    UNDEFINED = 0
    PURCHASE = 1
    CANCEL = -1

    LOG_TYPE = (
        (UNDEFINED, '미정'),
        (PURCHASE, '결제'),
        (CANCEL, '결제 취소'),
    )

    log_type = models.IntegerField(choices=LOG_TYPE, default=UNDEFINED)
    food_product = models.ForeignKey('app_model.FoodProduct', related_name='purchase_logs', on_delete=models.CASCADE)
    food_order = models.ForeignKey('app_model.FoodOrder', related_name='food_product_purchase_logs',
                                   on_delete=models.CASCADE)
    count = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_foodproductpurchaselog'


class FoodProductStock(models.Model):
    food_product = models.OneToOneField('app_model.FoodProduct', related_name='stock', on_delete=models.CASCADE)
    shipping_product = models.OneToOneField(ShippingProduct, related_name='stock', on_delete=models.CASCADE)

    limit_type = models.IntegerField(choices=LIMIT_TYPE, default=LimitType.STORAGE)

    # 재고형 limit field
    safety_stock = models.IntegerField(
        help_text='안전재고. 해당 값보다 아래면 is_available을 False 처리합니다.', null=True, default=None
    )
    proper_stock = models.IntegerField(
        help_text='적정재고. 해당 값보다 아래면 alarm을 합니다.', null=True, default=None
    )

    # rotation형 limit field
    expiration_day = models.IntegerField(
        null=True,
        help_text='유통기한 기간입니다. FoodProductOrderLimit의 manufactured_at과 연동하여 validated_at를 처리합니다',
        default=None
    )
    rotation_day = models.IntegerField(
        null=True, default=None,
        help_text='''rotation limit이 돌아가는 주기입니다. 
        만약 14일이면 새로운 FoodProductOrderLimit 생성할 때, 기존 것에 start_at과 end_at을 14일을 더합니다.'''
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'oms_foodproductstock'


class FoodProductStockLog(models.Model):
    """
    사방넷 : deprecated
    """
    """
    특정 시점의 재고입니다.
    필드명은 사방넷을 따라갑니다.
    """
    stock = models.ForeignKey(FoodProductStock, related_name='logs', on_delete=models.CASCADE)
    total_stock = models.IntegerField(default=0, help_text='총재고')
    receiving_stock = models.IntegerField(default=0, help_text='입고 재고')
    normal_stock = models.IntegerField(default=0, help_text='출고가능 재고')
    order_stock = models.IntegerField(default=0, help_text='출고지시 재고')
    shipping_stock = models.IntegerField(default=0, help_text='출고작업중 재고')
    damaged_stock = models.IntegerField(default=0, help_text='불량재고')
    return_stock = models.IntegerField(default=0, help_text='반품재고')
    keeping_stock = models.IntegerField(default=0, help_text='보관재고')

    request_at = models.DateTimeField(
        db_index=True,
        help_text='특정 시점을 적어주면 좋습니다. created_at으로 처리하는 것과 별개로 로직적인 이유로 적어주세요.',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
