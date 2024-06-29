from __future__ import annotations

from typing import Optional, Sequence

__doc__: str
__version__: str

class InvalidFlatbuffer(ValueError): ...

class AirState:
    OnGround = AirState(0)
    Jumping = AirState(1)
    DoubleJumping = AirState(2)
    Dodging = AirState(3)
    InAir = AirState(4)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: AirState) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> AirState:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BallAnchor:
    local: Vector3

    __match_args__ = (
        "local",
    )

    def __init__(
        self,
        local: Vector3 = Vector3(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallAnchor:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BallBouncinessOption:
    Default = BallBouncinessOption(0)
    Low = BallBouncinessOption(1)
    High = BallBouncinessOption(2)
    Super_High = BallBouncinessOption(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: BallBouncinessOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallBouncinessOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BallInfo:
    physics: Physics
    latest_touch: Touch
    shape: CollisionShape

    __match_args__ = (
        "physics",
        "latest_touch",
        "shape",
    )

    def __init__(
        self,
        physics: Physics = Physics(),
        latest_touch: Touch = Touch(),
        shape: Optional[BoxShape | SphereShape | CylinderShape] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallInfo:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BallMaxSpeedOption:
    Default = BallMaxSpeedOption(0)
    Slow = BallMaxSpeedOption(1)
    Fast = BallMaxSpeedOption(2)
    Super_Fast = BallMaxSpeedOption(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: BallMaxSpeedOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallMaxSpeedOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BallPrediction:
    slices: Sequence[PredictionSlice]

    __match_args__ = (
        "slices",
    )

    def __init__(
        self,
        slices: Sequence[PredictionSlice] = [],
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallPrediction:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BallSizeOption:
    Default = BallSizeOption(0)
    Small = BallSizeOption(1)
    Large = BallSizeOption(2)
    Gigantic = BallSizeOption(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: BallSizeOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallSizeOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BallTypeOption:
    Default = BallTypeOption(0)
    Cube = BallTypeOption(1)
    Puck = BallTypeOption(2)
    Basketball = BallTypeOption(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: BallTypeOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallTypeOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BallWeightOption:
    Default = BallWeightOption(0)
    Light = BallWeightOption(1)
    Heavy = BallWeightOption(2)
    Super_Light = BallWeightOption(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: BallWeightOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallWeightOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Bool:
    val: bool

    __match_args__ = (
        "val",
    )

    def __init__(
        self,
        val: bool = False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Bool:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BoostOption:
    Normal_Boost = BoostOption(0)
    Unlimited_Boost = BoostOption(1)
    Slow_Recharge = BoostOption(2)
    Rapid_Recharge = BoostOption(3)
    No_Boost = BoostOption(4)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: BoostOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoostOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BoostPad:
    location: Vector3
    is_full_boost: bool

    __match_args__ = (
        "location",
        "is_full_boost",
    )

    def __init__(
        self,
        location: Vector3 = Vector3(),
        is_full_boost: bool = False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoostPad:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BoostPadState:
    is_active: bool
    timer: float

    __match_args__ = (
        "is_active",
        "timer",
    )

    def __init__(
        self,
        is_active: bool = False,
        timer: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoostPadState:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BoostStrengthOption:
    One = BoostStrengthOption(0)
    OneAndAHalf = BoostStrengthOption(1)
    Two = BoostStrengthOption(2)
    Ten = BoostStrengthOption(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: BoostStrengthOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoostStrengthOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class BoxShape:
    length: float
    width: float
    height: float

    __match_args__ = (
        "length",
        "width",
        "height",
    )

    def __init__(
        self,
        length: float = 0,
        width: float = 0,
        height: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoxShape:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class CarAnchor:
    index: int
    local: Vector3

    __match_args__ = (
        "index",
        "local",
    )

    def __init__(
        self,
        index: int = 0,
        local: Vector3 = Vector3(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> CarAnchor:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class CollisionShape:
    item: Optional[BoxShape | SphereShape | CylinderShape]

    def __init__(
        self, item: Optional[BoxShape | SphereShape | CylinderShape] = None
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class Color:
    a: int
    r: int
    g: int
    b: int

    __match_args__ = (
        "a",
        "r",
        "g",
        "b",
    )

    def __init__(
        self,
        a: int = 0,
        r: int = 0,
        g: int = 0,
        b: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Color:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class ConsoleCommand:
    command: str

    __match_args__ = (
        "command",
    )

    def __init__(
        self,
        command: str = "",
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ConsoleCommand:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class ControllerState:
    throttle: float
    steer: float
    pitch: float
    yaw: float
    roll: float
    jump: bool
    boost: bool
    handbrake: bool
    use_item: bool

    __match_args__ = (
        "throttle",
        "steer",
        "pitch",
        "yaw",
        "roll",
        "jump",
        "boost",
        "handbrake",
        "use_item",
    )

    def __init__(
        self,
        throttle: float = 0,
        steer: float = 0,
        pitch: float = 0,
        yaw: float = 0,
        roll: float = 0,
        jump: bool = False,
        boost: bool = False,
        handbrake: bool = False,
        use_item: bool = False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ControllerState:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class CylinderShape:
    diameter: float
    height: float

    __match_args__ = (
        "diameter",
        "height",
    )

    def __init__(
        self,
        diameter: float = 0,
        height: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> CylinderShape:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class DemolishOption:
    Default = DemolishOption(0)
    Disabled = DemolishOption(1)
    Friendly_Fire = DemolishOption(2)
    On_Contact = DemolishOption(3)
    On_Contact_FF = DemolishOption(4)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: DemolishOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DemolishOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class DesiredBallState:
    physics: DesiredPhysics

    __match_args__ = (
        "physics",
    )

    def __init__(
        self,
        physics: DesiredPhysics = DesiredPhysics(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredBallState:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class DesiredBoostState:
    respawn_time: Optional[Float]

    __match_args__ = (
        "respawn_time",
    )

    def __init__(
        self,
        respawn_time: Optional[Float | float] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredBoostState:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class DesiredCarState:
    physics: Optional[DesiredPhysics]
    boost_amount: Optional[Float]

    __match_args__ = (
        "physics",
        "boost_amount",
    )

    def __init__(
        self,
        physics: Optional[DesiredPhysics] = None,
        boost_amount: Optional[Float | float] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredCarState:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class DesiredGameInfoState:
    world_gravity_z: Optional[Float]
    game_speed: Optional[Float]
    paused: Optional[Bool]
    end_match: Optional[Bool]

    __match_args__ = (
        "world_gravity_z",
        "game_speed",
        "paused",
        "end_match",
    )

    def __init__(
        self,
        world_gravity_z: Optional[Float | float] = None,
        game_speed: Optional[Float | float] = None,
        paused: Optional[Bool | bool] = None,
        end_match: Optional[Bool | bool] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredGameInfoState:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class DesiredGameState:
    ball_state: Optional[DesiredBallState]
    car_states: Sequence[DesiredCarState]
    boost_states: Sequence[DesiredBoostState]
    game_info_state: Optional[DesiredGameInfoState]
    console_commands: Sequence[ConsoleCommand]

    __match_args__ = (
        "ball_state",
        "car_states",
        "boost_states",
        "game_info_state",
        "console_commands",
    )

    def __init__(
        self,
        ball_state: Optional[DesiredBallState] = None,
        car_states: Sequence[DesiredCarState] = [],
        boost_states: Sequence[DesiredBoostState] = [],
        game_info_state: Optional[DesiredGameInfoState] = None,
        console_commands: Sequence[ConsoleCommand] = [],
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredGameState:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class DesiredPhysics:
    location: Optional[Vector3Partial]
    rotation: Optional[RotatorPartial]
    velocity: Optional[Vector3Partial]
    angular_velocity: Optional[Vector3Partial]

    __match_args__ = (
        "location",
        "rotation",
        "velocity",
        "angular_velocity",
    )

    def __init__(
        self,
        location: Optional[Vector3Partial] = None,
        rotation: Optional[RotatorPartial] = None,
        velocity: Optional[Vector3Partial] = None,
        angular_velocity: Optional[Vector3Partial] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredPhysics:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class ExistingMatchBehavior:
    Restart_If_Different = ExistingMatchBehavior(0)
    Restart = ExistingMatchBehavior(1)
    Continue_And_Spawn = ExistingMatchBehavior(2)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: ExistingMatchBehavior) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ExistingMatchBehavior:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class FieldInfo:
    boost_pads: Sequence[BoostPad]
    goals: Sequence[GoalInfo]

    __match_args__ = (
        "boost_pads",
        "goals",
    )

    def __init__(
        self,
        boost_pads: Sequence[BoostPad] = [],
        goals: Sequence[GoalInfo] = [],
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> FieldInfo:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Float:
    val: float

    __match_args__ = (
        "val",
    )

    def __init__(
        self,
        val: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Float:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class GameInfo:
    seconds_elapsed: float
    game_time_remaining: float
    is_overtime: bool
    is_unlimited_time: bool
    game_state_type: GameStateType
    world_gravity_z: float
    game_speed: float
    frame_num: int

    __match_args__ = (
        "seconds_elapsed",
        "game_time_remaining",
        "is_overtime",
        "is_unlimited_time",
        "game_state_type",
        "world_gravity_z",
        "game_speed",
        "frame_num",
    )

    def __init__(
        self,
        seconds_elapsed: float = 0,
        game_time_remaining: float = 0,
        is_overtime: bool = False,
        is_unlimited_time: bool = False,
        game_state_type: GameStateType = GameStateType(),
        world_gravity_z: float = 0,
        game_speed: float = 0,
        frame_num: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameInfo:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class GameMessage:
    item: Optional[PlayerStatEvent | PlayerSpectate | PlayerInputChange]

    def __init__(
        self, item: Optional[PlayerStatEvent | PlayerSpectate | PlayerInputChange] = None
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class GameMessageWrapper:
    message: GameMessage

    __match_args__ = (
        "message",
    )

    def __init__(
        self,
        message: Optional[PlayerStatEvent | PlayerSpectate | PlayerInputChange] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameMessageWrapper:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class GameMode:
    Soccer = GameMode(0)
    Hoops = GameMode(1)
    Dropshot = GameMode(2)
    Hockey = GameMode(3)
    Rumble = GameMode(4)
    Heatseeker = GameMode(5)
    Gridiron = GameMode(6)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: GameMode) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameMode:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class GameSpeedOption:
    Default = GameSpeedOption(0)
    Slo_Mo = GameSpeedOption(1)
    Time_Warp = GameSpeedOption(2)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: GameSpeedOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameSpeedOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class GameStateType:
    Inactive = GameStateType(0)
    Countdown = GameStateType(1)
    Kickoff = GameStateType(2)
    Active = GameStateType(3)
    GoalScored = GameStateType(4)
    Replay = GameStateType(5)
    Paused = GameStateType(6)
    Ended = GameStateType(7)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: GameStateType) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameStateType:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class GameTickPacket:
    players: Sequence[PlayerInfo]
    boost_pad_states: Sequence[BoostPadState]
    ball: BallInfo
    game_info: GameInfo
    teams: Sequence[TeamInfo]

    __match_args__ = (
        "players",
        "boost_pad_states",
        "ball",
        "game_info",
        "teams",
    )

    def __init__(
        self,
        players: Sequence[PlayerInfo] = [],
        boost_pad_states: Sequence[BoostPadState] = [],
        ball: BallInfo = BallInfo(),
        game_info: GameInfo = GameInfo(),
        teams: Sequence[TeamInfo] = [],
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameTickPacket:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class GoalInfo:
    team_num: int
    location: Vector3
    direction: Vector3
    width: float
    height: float

    __match_args__ = (
        "team_num",
        "location",
        "direction",
        "width",
        "height",
    )

    def __init__(
        self,
        team_num: int = 0,
        location: Vector3 = Vector3(),
        direction: Vector3 = Vector3(),
        width: float = 0,
        height: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GoalInfo:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class GravityOption:
    Default = GravityOption(0)
    Low = GravityOption(1)
    High = GravityOption(2)
    Super_High = GravityOption(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: GravityOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GravityOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Human:
    def __init__(self): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Human:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Launcher:
    Steam = Launcher(0)
    Epic = Launcher(1)
    Custom = Launcher(2)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: Launcher) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Launcher:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Line3D:
    start: RenderAnchor
    end: RenderAnchor
    color: Color

    __match_args__ = (
        "start",
        "end",
        "color",
    )

    def __init__(
        self,
        start: RenderAnchor = RenderAnchor(),
        end: RenderAnchor = RenderAnchor(),
        color: Color = Color(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Line3D:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class LoadoutPaint:
    car_paint_id: int
    decal_paint_id: int
    wheels_paint_id: int
    boost_paint_id: int
    antenna_paint_id: int
    hat_paint_id: int
    trails_paint_id: int
    goal_explosion_paint_id: int

    __match_args__ = (
        "car_paint_id",
        "decal_paint_id",
        "wheels_paint_id",
        "boost_paint_id",
        "antenna_paint_id",
        "hat_paint_id",
        "trails_paint_id",
        "goal_explosion_paint_id",
    )

    def __init__(
        self,
        car_paint_id: int = 0,
        decal_paint_id: int = 0,
        wheels_paint_id: int = 0,
        boost_paint_id: int = 0,
        antenna_paint_id: int = 0,
        hat_paint_id: int = 0,
        trails_paint_id: int = 0,
        goal_explosion_paint_id: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> LoadoutPaint:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class MatchComm:
    index: int
    team: int
    team_only: bool
    display: Optional[str]
    content: bytes

    __match_args__ = (
        "index",
        "team",
        "team_only",
        "display",
        "content",
    )

    def __init__(
        self,
        index: int = 0,
        team: int = 0,
        team_only: bool = False,
        display: Optional[str] = None,
        content: bytes = b"",
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MatchComm:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class MatchLength:
    Five_Minutes = MatchLength(0)
    Ten_Minutes = MatchLength(1)
    Twenty_Minutes = MatchLength(2)
    Unlimited = MatchLength(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: MatchLength) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MatchLength:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class MatchSettings:
    launcher: Launcher
    game_path: str
    auto_start_bots: bool
    game_map_upk: str
    player_configurations: Sequence[PlayerConfiguration]
    script_configurations: Sequence[ScriptConfiguration]
    game_mode: GameMode
    skip_replays: bool
    instant_start: bool
    mutator_settings: Optional[MutatorSettings]
    existing_match_behavior: ExistingMatchBehavior
    enable_rendering: bool
    enable_state_setting: bool
    auto_save_replay: bool

    __match_args__ = (
        "launcher",
        "game_path",
        "auto_start_bots",
        "game_map_upk",
        "player_configurations",
        "script_configurations",
        "game_mode",
        "skip_replays",
        "instant_start",
        "mutator_settings",
        "existing_match_behavior",
        "enable_rendering",
        "enable_state_setting",
        "auto_save_replay",
    )

    def __init__(
        self,
        launcher: Launcher = Launcher(),
        game_path: str = "",
        auto_start_bots: bool = False,
        game_map_upk: str = "",
        player_configurations: Sequence[PlayerConfiguration] = [],
        script_configurations: Sequence[ScriptConfiguration] = [],
        game_mode: GameMode = GameMode(),
        skip_replays: bool = False,
        instant_start: bool = False,
        mutator_settings: Optional[MutatorSettings] = None,
        existing_match_behavior: ExistingMatchBehavior = ExistingMatchBehavior(),
        enable_rendering: bool = False,
        enable_state_setting: bool = False,
        auto_save_replay: bool = False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MatchSettings:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class MaxScore:
    Unlimited = MaxScore(0)
    One_Goal = MaxScore(1)
    Three_Goals = MaxScore(2)
    Five_Goals = MaxScore(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: MaxScore) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MaxScore:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class MessagePacket:
    messages: Sequence[GameMessageWrapper]
    game_seconds: float
    frame_num: int

    __match_args__ = (
        "messages",
        "game_seconds",
        "frame_num",
    )

    def __init__(
        self,
        messages: Sequence[GameMessageWrapper] = [],
        game_seconds: float = 0,
        frame_num: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MessagePacket:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class MutatorSettings:
    match_length: MatchLength
    max_score: MaxScore
    overtime_option: OvertimeOption
    series_length_option: SeriesLengthOption
    game_speed_option: GameSpeedOption
    ball_max_speed_option: BallMaxSpeedOption
    ball_type_option: BallTypeOption
    ball_weight_option: BallWeightOption
    ball_size_option: BallSizeOption
    ball_bounciness_option: BallBouncinessOption
    boost_option: BoostOption
    rumble_option: RumbleOption
    boost_strength_option: BoostStrengthOption
    gravity_option: GravityOption
    demolish_option: DemolishOption
    respawn_time_option: RespawnTimeOption

    __match_args__ = (
        "match_length",
        "max_score",
        "overtime_option",
        "series_length_option",
        "game_speed_option",
        "ball_max_speed_option",
        "ball_type_option",
        "ball_weight_option",
        "ball_size_option",
        "ball_bounciness_option",
        "boost_option",
        "rumble_option",
        "boost_strength_option",
        "gravity_option",
        "demolish_option",
        "respawn_time_option",
    )

    def __init__(
        self,
        match_length: MatchLength = MatchLength(),
        max_score: MaxScore = MaxScore(),
        overtime_option: OvertimeOption = OvertimeOption(),
        series_length_option: SeriesLengthOption = SeriesLengthOption(),
        game_speed_option: GameSpeedOption = GameSpeedOption(),
        ball_max_speed_option: BallMaxSpeedOption = BallMaxSpeedOption(),
        ball_type_option: BallTypeOption = BallTypeOption(),
        ball_weight_option: BallWeightOption = BallWeightOption(),
        ball_size_option: BallSizeOption = BallSizeOption(),
        ball_bounciness_option: BallBouncinessOption = BallBouncinessOption(),
        boost_option: BoostOption = BoostOption(),
        rumble_option: RumbleOption = RumbleOption(),
        boost_strength_option: BoostStrengthOption = BoostStrengthOption(),
        gravity_option: GravityOption = GravityOption(),
        demolish_option: DemolishOption = DemolishOption(),
        respawn_time_option: RespawnTimeOption = RespawnTimeOption(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MutatorSettings:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class OvertimeOption:
    Unlimited = OvertimeOption(0)
    Five_Max_First_Score = OvertimeOption(1)
    Five_Max_Random_Team = OvertimeOption(2)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: OvertimeOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> OvertimeOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PartyMember:
    def __init__(self): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PartyMember:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Physics:
    location: Vector3
    rotation: Rotator
    velocity: Vector3
    angular_velocity: Vector3

    __match_args__ = (
        "location",
        "rotation",
        "velocity",
        "angular_velocity",
    )

    def __init__(
        self,
        location: Vector3 = Vector3(),
        rotation: Rotator = Rotator(),
        velocity: Vector3 = Vector3(),
        angular_velocity: Vector3 = Vector3(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Physics:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PlayerClass:
    item: Optional[RLBot | Human | Psyonix | PartyMember]

    def __init__(
        self, item: Optional[RLBot | Human | Psyonix | PartyMember] = None
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class PlayerConfiguration:
    variety: PlayerClass
    name: str
    team: int
    location: str
    run_command: str
    loadout: Optional[PlayerLoadout]
    spawn_id: int

    __match_args__ = (
        "variety",
        "name",
        "team",
        "location",
        "run_command",
        "loadout",
        "spawn_id",
    )

    def __init__(
        self,
        variety: Optional[RLBot | Human | Psyonix | PartyMember] = None,
        name: str = "",
        team: int = 0,
        location: str = "",
        run_command: str = "",
        loadout: Optional[PlayerLoadout] = None,
        spawn_id: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerConfiguration:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PlayerInfo:
    physics: Physics
    score_info: ScoreInfo
    hitbox: BoxShape
    hitbox_offset: Vector3
    air_state: AirState
    dodge_timeout: float
    demolished_timeout: float
    is_supersonic: bool
    is_bot: bool
    name: str
    team: int
    boost: int
    spawn_id: int

    __match_args__ = (
        "physics",
        "score_info",
        "hitbox",
        "hitbox_offset",
        "air_state",
        "dodge_timeout",
        "demolished_timeout",
        "is_supersonic",
        "is_bot",
        "name",
        "team",
        "boost",
        "spawn_id",
    )

    def __init__(
        self,
        physics: Physics = Physics(),
        score_info: ScoreInfo = ScoreInfo(),
        hitbox: BoxShape = BoxShape(),
        hitbox_offset: Vector3 = Vector3(),
        air_state: AirState = AirState(),
        dodge_timeout: float = 0,
        demolished_timeout: float = 0,
        is_supersonic: bool = False,
        is_bot: bool = False,
        name: str = "",
        team: int = 0,
        boost: int = 0,
        spawn_id: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerInfo:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PlayerInput:
    player_index: int
    controller_state: ControllerState

    __match_args__ = (
        "player_index",
        "controller_state",
    )

    def __init__(
        self,
        player_index: int = 0,
        controller_state: ControllerState = ControllerState(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerInput:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PlayerInputChange:
    player_index: int
    controller_state: ControllerState
    dodge_forward: float
    dodge_right: float

    __match_args__ = (
        "player_index",
        "controller_state",
        "dodge_forward",
        "dodge_right",
    )

    def __init__(
        self,
        player_index: int = 0,
        controller_state: ControllerState = ControllerState(),
        dodge_forward: float = 0,
        dodge_right: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerInputChange:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PlayerLoadout:
    team_color_id: int
    custom_color_id: int
    car_id: int
    decal_id: int
    wheels_id: int
    boost_id: int
    antenna_id: int
    hat_id: int
    paint_finish_id: int
    custom_finish_id: int
    engine_audio_id: int
    trails_id: int
    goal_explosion_id: int
    loadout_paint: Optional[LoadoutPaint]
    primary_color_lookup: Optional[Color]
    secondary_color_lookup: Optional[Color]

    __match_args__ = (
        "team_color_id",
        "custom_color_id",
        "car_id",
        "decal_id",
        "wheels_id",
        "boost_id",
        "antenna_id",
        "hat_id",
        "paint_finish_id",
        "custom_finish_id",
        "engine_audio_id",
        "trails_id",
        "goal_explosion_id",
        "loadout_paint",
        "primary_color_lookup",
        "secondary_color_lookup",
    )

    def __init__(
        self,
        team_color_id: int = 0,
        custom_color_id: int = 0,
        car_id: int = 0,
        decal_id: int = 0,
        wheels_id: int = 0,
        boost_id: int = 0,
        antenna_id: int = 0,
        hat_id: int = 0,
        paint_finish_id: int = 0,
        custom_finish_id: int = 0,
        engine_audio_id: int = 0,
        trails_id: int = 0,
        goal_explosion_id: int = 0,
        loadout_paint: Optional[LoadoutPaint] = None,
        primary_color_lookup: Optional[Color] = None,
        secondary_color_lookup: Optional[Color] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerLoadout:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PlayerSpectate:
    player_index: int

    __match_args__ = (
        "player_index",
    )

    def __init__(
        self,
        player_index: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerSpectate:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PlayerStatEvent:
    player_index: int
    stat_type: str

    __match_args__ = (
        "player_index",
        "stat_type",
    )

    def __init__(
        self,
        player_index: int = 0,
        stat_type: str = "",
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerStatEvent:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PolyLine3D:
    points: Sequence[Vector3]
    color: Color

    __match_args__ = (
        "points",
        "color",
    )

    def __init__(
        self,
        points: Sequence[Vector3] = [],
        color: Color = Color(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PolyLine3D:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class PredictionSlice:
    game_seconds: float
    physics: Physics

    __match_args__ = (
        "game_seconds",
        "physics",
    )

    def __init__(
        self,
        game_seconds: float = 0,
        physics: Physics = Physics(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PredictionSlice:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Psyonix:
    bot_skill: float

    __match_args__ = (
        "bot_skill",
    )

    def __init__(
        self,
        bot_skill: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Psyonix:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class RLBot:
    def __init__(self): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RLBot:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class ReadyMessage:
    wants_ball_predictions: bool
    wants_comms: bool
    wants_game_messages: bool
    close_after_match: bool

    __match_args__ = (
        "wants_ball_predictions",
        "wants_comms",
        "wants_game_messages",
        "close_after_match",
    )

    def __init__(
        self,
        wants_ball_predictions: bool = False,
        wants_comms: bool = False,
        wants_game_messages: bool = False,
        close_after_match: bool = False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ReadyMessage:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class RelativeAnchor:
    item: Optional[BallAnchor | CarAnchor]

    def __init__(
        self, item: Optional[BallAnchor | CarAnchor] = None
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class RemoveRenderGroup:
    id: int

    __match_args__ = (
        "id",
    )

    def __init__(
        self,
        id: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RemoveRenderGroup:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class RenderAnchor:
    world: Vector3
    relative: RelativeAnchor

    __match_args__ = (
        "world",
        "relative",
    )

    def __init__(
        self,
        world: Vector3 = Vector3(),
        relative: Optional[BallAnchor | CarAnchor] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RenderAnchor:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class RenderGroup:
    render_messages: Sequence[RenderMessage]
    id: int

    __match_args__ = (
        "render_messages",
        "id",
    )

    def __init__(
        self,
        render_messages: Sequence[RenderMessage] = [],
        id: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RenderGroup:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class RenderMessage:
    variety: RenderType

    __match_args__ = (
        "variety",
    )

    def __init__(
        self,
        variety: Optional[Line3D | PolyLine3D | String2D | String3D] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RenderMessage:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class RenderType:
    item: Optional[Line3D | PolyLine3D | String2D | String3D]

    def __init__(
        self, item: Optional[Line3D | PolyLine3D | String2D | String3D] = None
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class RespawnTimeOption:
    Three_Seconds = RespawnTimeOption(0)
    Two_Seconds = RespawnTimeOption(1)
    One_Seconds = RespawnTimeOption(2)
    Disable_Goal_Reset = RespawnTimeOption(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: RespawnTimeOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RespawnTimeOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Rotator:
    pitch: float
    yaw: float
    roll: float

    __match_args__ = (
        "pitch",
        "yaw",
        "roll",
    )

    def __init__(
        self,
        pitch: float = 0,
        yaw: float = 0,
        roll: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Rotator:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class RotatorPartial:
    pitch: Optional[Float]
    yaw: Optional[Float]
    roll: Optional[Float]

    __match_args__ = (
        "pitch",
        "yaw",
        "roll",
    )

    def __init__(
        self,
        pitch: Optional[Float | float] = None,
        yaw: Optional[Float | float] = None,
        roll: Optional[Float | float] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RotatorPartial:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class RumbleOption:
    No_Rumble = RumbleOption(0)
    Default = RumbleOption(1)
    Slow = RumbleOption(2)
    Civilized = RumbleOption(3)
    Destruction_Derby = RumbleOption(4)
    Spring_Loaded = RumbleOption(5)
    Spikes_Only = RumbleOption(6)
    Spike_Rush = RumbleOption(7)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: RumbleOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RumbleOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class ScoreInfo:
    score: int
    goals: int
    own_goals: int
    assists: int
    saves: int
    shots: int
    demolitions: int

    __match_args__ = (
        "score",
        "goals",
        "own_goals",
        "assists",
        "saves",
        "shots",
        "demolitions",
    )

    def __init__(
        self,
        score: int = 0,
        goals: int = 0,
        own_goals: int = 0,
        assists: int = 0,
        saves: int = 0,
        shots: int = 0,
        demolitions: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ScoreInfo:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class ScriptConfiguration:
    location: str
    run_command: str

    __match_args__ = (
        "location",
        "run_command",
    )

    def __init__(
        self,
        location: str = "",
        run_command: str = "",
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ScriptConfiguration:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class SeriesLengthOption:
    Unlimited = SeriesLengthOption(0)
    Three_Games = SeriesLengthOption(1)
    Five_Games = SeriesLengthOption(2)
    Seven_Games = SeriesLengthOption(3)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: SeriesLengthOption) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> SeriesLengthOption:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class SphereShape:
    diameter: float

    __match_args__ = (
        "diameter",
    )

    def __init__(
        self,
        diameter: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> SphereShape:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class StartCommand:
    config_path: str

    __match_args__ = (
        "config_path",
    )

    def __init__(
        self,
        config_path: str = "",
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> StartCommand:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class StopCommand:
    shutdown_server: bool

    __match_args__ = (
        "shutdown_server",
    )

    def __init__(
        self,
        shutdown_server: bool = False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> StopCommand:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class String2D:
    text: str
    x: float
    y: float
    scale: float
    foreground: Color
    background: Color
    h_align: TextHAlign
    v_align: TextVAlign

    __match_args__ = (
        "text",
        "x",
        "y",
        "scale",
        "foreground",
        "background",
        "h_align",
        "v_align",
    )

    def __init__(
        self,
        text: str = "",
        x: float = 0,
        y: float = 0,
        scale: float = 0,
        foreground: Color = Color(),
        background: Color = Color(),
        h_align: TextHAlign = TextHAlign(),
        v_align: TextVAlign = TextVAlign(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> String2D:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class String3D:
    text: str
    anchor: RenderAnchor
    scale: float
    foreground: Color
    background: Color
    h_align: TextHAlign
    v_align: TextVAlign

    __match_args__ = (
        "text",
        "anchor",
        "scale",
        "foreground",
        "background",
        "h_align",
        "v_align",
    )

    def __init__(
        self,
        text: str = "",
        anchor: RenderAnchor = RenderAnchor(),
        scale: float = 0,
        foreground: Color = Color(),
        background: Color = Color(),
        h_align: TextHAlign = TextHAlign(),
        v_align: TextVAlign = TextVAlign(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> String3D:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class TeamInfo:
    team_index: int
    score: int

    __match_args__ = (
        "team_index",
        "score",
    )

    def __init__(
        self,
        team_index: int = 0,
        score: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> TeamInfo:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class TextHAlign:
    Left = TextHAlign(0)
    Center = TextHAlign(1)
    Right = TextHAlign(2)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: TextHAlign) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> TextHAlign:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class TextVAlign:
    Top = TextVAlign(0)
    Center = TextVAlign(1)
    Bottom = TextVAlign(2)

    def __init__(self, value: int = 0):
        """
        :raises ValueError: If the `value` is not a valid enum value
        """

    def __int__(self) -> int: ...
    def __eq__(self, other: TextVAlign) -> bool: ...
    def __hash__(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> TextVAlign:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Touch:
    player_name: str
    game_seconds: float
    location: Vector3
    normal: Vector3
    team: int
    player_index: int

    __match_args__ = (
        "player_name",
        "game_seconds",
        "location",
        "normal",
        "team",
        "player_index",
    )

    def __init__(
        self,
        player_name: str = "",
        game_seconds: float = 0,
        location: Vector3 = Vector3(),
        normal: Vector3 = Vector3(),
        team: int = 0,
        player_index: int = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Touch:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Vector3:
    x: float
    y: float
    z: float

    __match_args__ = (
        "x",
        "y",
        "z",
    )

    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Vector3:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """

class Vector3Partial:
    x: Optional[Float]
    y: Optional[Float]
    z: Optional[Float]

    __match_args__ = (
        "x",
        "y",
        "z",
    )

    def __init__(
        self,
        x: Optional[Float | float] = None,
        y: Optional[Float | float] = None,
        z: Optional[Float | float] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Vector3Partial:
        """
        :raises InvalidFlatbuffer: If the `data` is invalid for this type
        """
