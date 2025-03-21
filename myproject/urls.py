# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapi.views import ProductView, ItemView,ReceivedTransactionView,DepositToCashUpDaily,WithdrawalRequestFromCashupMonthlyAPIView,WithdrawalRequestFromDailyProfitAPIView,DepositToMonthlyDepositBalance,MobileRechargeView,DepositToDepositBalance,ResetPasswordView,SendMoneyView,SponsoredByCreateView,ProductAdSliderView,ReferralGetCodeView,CompoundingProfitHistoryListView,ChangePasswordView,CompanyNumberListView,WithdrawalHistoryView,WithdrawalRequestFromDailyProfitAPIView,WithdrawalRequestFromAffiliateProfitAPIView, ProfileView,ReferralCodeView,ForgotPasswordView,CashupDepositHistoryView,PlaceOrderView,CashupOwingProfitHistoryListView,WithdrawalRequestAPIView,CashupProfitHistoryListView,SliderCreateView,TransferToCashupOwingDPSView,WithdrawalRequestFromCompoundingProfitAPIView,WithdrawalRequestFromMianBalanceAPIView,CheckoutDetailsView, CartedProductDelete,BuyerView,RegisterView,LoginAPIView,SendOTPToBuyer,VerifyBuyerOTP,BuyerDetail,BuyerTransactionCreateView, UpdateBuyerProfileAPIView, DepositToMainBalance, TransferToCashupDeposit, TransferToCashupOwingDeposit, PurchaseProduct,ConfirmedProductsList,CashupOwingDepositByBuyerAPIView,CashupDepositByBuyerAPIView,ConfirmedBuyersForProducts,BuyerPurchasesAPIView , ConfirmedBuyerView,ProductDetail, CartedProductsList
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView 
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header= 'CashUp'
admin.site.index_title='Welcome to Cashup'



# Create a default router and register your viewsets
router = DefaultRouter()
router.register(r'purchase', ProductView)
router.register(r'buyers', BuyerView)
router.register(r'items', ItemView)


# Define the urlpatterns with the additional views included
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/confirmed-products/', ConfirmedProductsList.as_view(), name='confirmed-products'),
    path('api/carted-products/', CartedProductsList.as_view(), name='carted-products'),
    path('api/product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api/confirmed-buyers/', ConfirmedBuyerView.as_view(), name='confirmed-buyer'),
    path('api/confirmed-buyersforproduct/', ConfirmedBuyersForProducts.as_view(), name='confirmed-buyersforproduct'),
    path('api/buyer-purchases/', BuyerPurchasesAPIView.as_view(), name='buyer-purchases'),
    path('api/cashup-deposit/', CashupDepositByBuyerAPIView.as_view(), name='cashup-deposit'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('update-profile/', UpdateBuyerProfileAPIView.as_view(), name='update-profile'),
    path('api/deposit/', DepositToMainBalance.as_view(), name='deposit-to-main-balance'),
    path('api/transfer-to-cashup-deposit/', TransferToCashupDeposit.as_view(), name='transfer-to-cashup-deposit'),
    path('api/transfer-to-cashup-owing-deposit/', TransferToCashupOwingDeposit.as_view(), name='transfer-to-cashup-owing-deposit'),
    path('purchase/', PurchaseProduct.as_view(), name='purchase-product'),
    path('api/cashup-owing-deposit/', CashupOwingDepositByBuyerAPIView.as_view(), name='cashup-owing-deposits-by-buyer'),
    path('api/buyer/', BuyerDetail.as_view(), name='buyer-detail'),
    path('buyer_transactions/', BuyerTransactionCreateView.as_view(), name='buyer_transaction_create'),
    path('send-otp/', SendOTPToBuyer.as_view(), name='send-otp'),
    path('verify-otp/', VerifyBuyerOTP.as_view(), name='verify-otp'),
    path('api/me/', ProfileView.as_view(), name='profile'),
    path('api/remove_carted_products/<int:pk>/', CartedProductDelete.as_view(), name='carted-product-delete'),
    path('api/checkout-details/',CheckoutDetailsView.as_view(),name="checkout-details"),
    path('api/place-order/<int:pk>',PlaceOrderView.as_view(),name="place-order"),
    path('withdrawal-from-cashup-deposit/', WithdrawalRequestAPIView.as_view(), name='withdrawal-request'),
    path('withdrawal-from-main-balance/', WithdrawalRequestFromMianBalanceAPIView.as_view(), name='withdrawal-from-main-balance'),
    path('api/transfer-to-cashup-owing-dps/', TransferToCashupOwingDPSView.as_view(), name='transfer-to-cashup-owing-dps'),
    path('create-slider/', SliderCreateView.as_view(), name='create-slider'),
    path('cashup-profit-history/', CashupProfitHistoryListView.as_view(), name='cashup-profit-history'),
    path('cashup-owing-profit-history/', CashupOwingProfitHistoryListView.as_view(), name='cashup-owing-profit-history'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('generate-affliate-code/',ReferralCodeView.as_view(),name='generate-affliate-code'),
    path('withdraw-from-daily-profit/',WithdrawalRequestFromDailyProfitAPIView.as_view(),name='withdraw-from-daily-profit'),
    path('withdraw-from-affiliate-profit/',WithdrawalRequestFromAffiliateProfitAPIView.as_view(),name='withdraw-from-affiliate-profit'),
    path('compounding-profit-history/',CompoundingProfitHistoryListView.as_view(),name='compounding-profit-history'),
    path('withdrawal-history/',WithdrawalHistoryView.as_view(),name='withdrawal-history'),
    path('company-number/',CompanyNumberListView.as_view(),name='company-number'),
    path('change-password/',ChangePasswordView.as_view(),name='change-password'),
    path('refer-code/',ReferralGetCodeView.as_view(),name='refer-code'),
    path('product-ad-slider/',ProductAdSliderView.as_view(),name='refer-code'),
    path('sponsored-by/', SponsoredByCreateView.as_view(), name='sponsored-by'),
    path('send-money/',SendMoneyView.as_view(),name='send-money'),
    path('received-money/',ReceivedTransactionView.as_view(),name='recieve-money'),
    path('mobile-recharge/', MobileRechargeView.as_view(), name='mobile-recharge'),
    path('api/deposit-to-cashup-monthly-compounding/', DepositToDepositBalance.as_view(), name='deposit-to-cashup-monthly-compounding'),
    path('api/deposit-to-cashup-monthly/', DepositToMonthlyDepositBalance.as_view(), name='deposit-to-cashup-monthly'),
    path('api/withdraw-from-cashup-daily/', WithdrawalRequestFromDailyProfitAPIView.as_view(), name='withdraw-balance'),
    path('api/deposit-to-cashup-daily/', DepositToCashUpDaily.as_view(), name='deposit-to-cashup-daily'),
    path('withdrawal-from-compounding-profit/', WithdrawalRequestFromCompoundingProfitAPIView.as_view(), name='withdrawal-from-compounding-profit'),
    path('withdrawal-from-monthly-profit/', WithdrawalRequestFromCashupMonthlyAPIView.as_view(), name='withdrawal-from-monthly-profit'),
    
    
    

    

    

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

