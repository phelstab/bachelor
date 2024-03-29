from .examples.momentum_agent import MomentumAgent

from .market_makers.adaptive_market_maker_agent import AdaptiveMarketMakerAgent

from .exchange_agent import ExchangeAgent
from .financial_agent import FinancialAgent
from .noise_agent import NoiseAgent
from .trading_agent import TradingAgent
from .value_agent import ValueAgent


from .examples.new_momentum_agent import NewMomentumAgent


# from .new_value_agent import NewValueAgent
# from .new_noise_agent import NewNoiseAgent
# from .new_fundamental_tracking_agent import NewFundamentalTrackingAgent


from .new_exchange_agent import NewExchangeAgent
from .new_trading_agent import NewTradingAgent
from .dual_value_agent import DualValueAgent
from .intermarket_spread_arbitrage_machine import IntermarketSpreadArbitrageMachine
from .dual_momentum_agent import DualMomentumAgent
from .dual_noise_agent_0 import NoiseAgent_0
from .dual_noise_agent_1 import NoiseAgent_1

#from .new_beta_trading_agent import NewBetaTradingAgent


from .market_makers.new_adaptive_market_maker_agent import NewAdaptiveMarketMakerAgent

from .market_makers.adaptive_market_maker_agent_0 import AdaptiveMarketMakerAgent0
from .market_makers.adaptive_market_maker_agent_1 import AdaptiveMarketMakerAgent1


from .variable.var_momentum_agent import VarMomentumAgent
from .variable.var_noise_agent import VarNoiseAgent
from .variable.var_value_agent import VarValueAgent
from .variable.var_adaptive_market_maker_agent import VarAdaptiveMarketMakerAgent
from .makertaker.mt_momentum_agent import MTMomentumAgent
from .makertaker.mt_noise_agent import MTNoiseAgent
from .makertaker.mt_value_agent import MTValueAgent
from .makertaker.mt_adaptive_market_maker_agent import MTAdaptiveMarketMakerAgent
from .nofee.nf_adaptive_market_maker_agent import NFAdaptiveMarketMakerAgent
from .nofee.nf_momentum_agent import NFMomentumAgent
from .nofee.nf_noise_agent import NFNoiseAgent
from .nofee.nf_value_agent import NFValueAgent
from .nofee.nf_trading_agent import NFTradingAgent
from .fix.fix_adaptive_market_maker_agent import FixAdaptiveMarketMakerAgent
from .fix.fix_momentum_agent import FixMomentumAgent
from .fix.fix_noise_agent import FixNoiseAgent
from .fix.fix_value_agent import FixValueAgent
from .fix.fix_trading_agent import FixTradingAgent

from .execution.pov_execution_agent import POVExecutionAgent